# deepface — התקנה והרצה (Windows)

זיהוי **גיל / רגש** בזמן אמת מהמצלמה, מבוסס על [DeepFace](https://github.com/serengil/deepface).

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
python age.py        :: הערכת גיל חיה מהמצלמה
python emotion.py    :: זיהוי רגש חי מהמצלמה
```

בכל פתיחת חלון CMD חדש, הפעל קודם את הסביבה:
```bat
.venv\Scripts\activate
```

## הערות
- צריך **מצלמה** ו**מסך** (נפתח חלון OpenCV; לחיצה על `ESC` סוגרת).
- בהרצה הראשונה DeepFace מוריד משקלי מודל (~0.5 GB) אל `C:\Users\<שם>\.deepface\`.
- `deepface` מתקין **TensorFlow** מתאים אוטומטית; `tf-keras` נדרש עבור TensorFlow ≥ 2.16.
