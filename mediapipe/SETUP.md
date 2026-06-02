# mediapipe — התקנה והרצה (Windows)

הדגמות של זיהוי יד / פנים ומשחקים קטנים, מבוסס על
[MediaPipe](https://github.com/google/mediapipe).

## דרישה מקדימה
התקן **Python 3.12** מהאתר הרשמי: https://www.python.org/downloads/
בזמן ההתקנה סמן את התיבה **"Add Python to PATH"**. זה הכלי היחיד שצריך.

## התקנה (פעם אחת)
פתח **CMD** בתיקייה הזו והרץ:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirments.txt
```

## הרצה
כשהסביבה פעילה (מופיע `(.venv)` בתחילת השורה):

```bat
python app.py           :: מעקב אחר היד
python index.py         :: הדגמת נקודות ציון של היד
python snake.py         :: סנייק בשליטת מחוות
python flappyBird.py    :: פלאפי בירד בשליטת מחוות
```

בכל פתיחת חלון CMD חדש, הפעל קודם את הסביבה:
```bat
.venv\Scripts\activate
```

## הערות
- צריך **מצלמה** ו**מסך** (חלונות OpenCV / pygame).
- **חשוב לא לשנות את גרסת mediapipe:** החל מ-0.10.30 הוסר ה-API הישן `mp.solutions`.
  כל הסקריפטים כאן משתמשים ב-`mp.solutions.hands`, לכן `requirments.txt` מקבע
  `mediapipe>=0.10.14,<0.10.30`. אל תסיר את ההגבלה הזו.
- הפרויקט הזה **לא** כולל TensorFlow בכוונה: mediapipe דורש `protobuf<5` ואילו
  TensorFlow ≥ 2.20 דורש `protobuf>=5.28` — הם לא יכולים לדור יחד, והסקריפטים
  כאן לא משתמשים ב-TensorFlow.
