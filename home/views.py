from django.shortcuts import render
from accounts.models import User, Person, Counselor
from diary.models import Diary
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(redirect_field_name='login')
def home_view(request):
    user = request.user
    person = Person.objects.get(id=request.user.id)

    recent_diaries = Diary.objects.filter(user_id=user.id).order_by('-diary_write_date')[:5]
    # 감정 통계 데이터
    emotion_stats = (
        Diary.objects.filter(user_id=user.id)
        .values('emotion_analysis__happiness_score', 'emotion_analysis__sadness_score', 'emotion_analysis__anger_score',
                'emotion_analysis__anxiety_score', 'emotion_analysis__embarrassment_score', 'emotion_analysis__hurt_score')
        .all()
    )

    # 총합 계산
    emotion_totals = {
        "happiness": sum(e["emotion_analysis__happiness_score"] for e in emotion_stats),
        "sadness": sum(e["emotion_analysis__sadness_score"] for e in emotion_stats),
        "anger": sum(e["emotion_analysis__anger_score"] for e in emotion_stats),
        "anxiety": sum(e["emotion_analysis__anxiety_score"] for e in emotion_stats),
        "embarrassment": sum(e["emotion_analysis__embarrassment_score"] for e in emotion_stats),
        "hurt": sum(e["emotion_analysis__hurt_score"] for e in emotion_stats),
    }

    return render(request, "user/home.html", {
        "user": user,
        "recent_diaries": recent_diaries,
        "emotion_totals": emotion_totals,
        "person_role": person.role,
    })

def counselor_home(request):
    person = Person.objects.get(id=request.user.id)
    if person.role != 'counselor':
        messages.error(request, "상담사만 접근 가능합니다.")

    counselor = Counselor.objects.get(id=person)
    return render(request, 'counselor/counselor_home.html', {
        'person': person,
        'counselor': counselor,
        "person_role": person.role,
    })
