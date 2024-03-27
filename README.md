# Hadasim4
Hadasim 4 home exercise implementation 

תרגיל מספר 1:

מסד נתונים:
הישויות במסד הנתונים:
1.	חברים בקופת החולים Patient: קוד חבר (PK), תעודת זהות, שם פרטי, שם משפחה, תאריך לידה, קוד כתובת (FK), תמונה, סטטוס.
2.	כתובת חבר קו"ח Paddress: קוד כתובת(PK), קוד עיר (FK), רחוב, מספר בנין, מספר דירה.
3.	חולי sickness Period: קוד חולי (PKׂׂ), ת.ז חבר קו"ח (FK), תאריך גילוי, תאריך החלמה.
4. התחסנות: Vaccination: קוד חיסון (PK), ת.ז. חבר קו"ח (FK), קוד סוג חיסון (FK), תאריך.
6.	סוג החיסון: VaccinationType: קוד חיסון (PK), שם חיסון.
7.	ערים: City: קוד עיר (PK), שם עיר.

לצורך התקנת מסד הנתונים יש להריץ את השאילה המצורפת בקובץ HealthClinic.sql (נוסה הותקן בSQL SERVER).

לא לגמרי הסתדרתי עם ההעלאה של כל הקבצים לכאן, לכן העלתי גם לענן:
https://drive.google.com/drive/folders/1XF4DYWCJx1T6UzESmScSKQi3wfkxI_By?usp=sharing
