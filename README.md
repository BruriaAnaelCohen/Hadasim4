# Hadasim4
Hadasim 4 home exercise implementation 

לא לגמרי הסתדרתי עם ההעלאה של כל הקבצים לכאן, לכן העלתי גם לענן:
https://drive.google.com/drive/folders/1XF4DYWCJx1T6UzESmScSKQi3wfkxI_By?usp=sharing
שם מסודרים הקבצים טוב יותר. (מצטערת, לא ידעתי איך להסיר קבצים מהRepository.
תרגיל מספר 1 מופיע כאן כקובץ ZIP בשם Exersice 1, בגלל גדלו היה קשה להעלות אותו (אם יש בעיה איתו, יש עותק שלו בGOOGLE DRIVE, קישור לעיל).
תרגיל מספר 2 מופיע בתקיה בשם Exercise 2, שדרוג שלו מופיע בקובץ פייתון בודד בשם Exercise 2 Twitter towwers using OOP updated.py
תרגיל מספר 3 מופיע כקובץ WORD בשם 
תרגיל מספר 1:

**מסד נתונים: **
מסד הנתונים שלהלן נעשה בSQL SERVER.
הישויות במסד הנתונים:
1.	חברים בקופת החולים Patient: קוד חבר (PK), תעודת זהות, שם פרטי, שם משפחה, תאריך לידה, קוד כתובת (FK), תמונה, סטטוס.
2.	כתובת חבר קו"ח Paddress: קוד כתובת(PK), קוד עיר (FK), רחוב, מספר בנין, מספר דירה.
3.	חולי sickness Period: קוד חולי (PKׂׂ), ת.ז חבר קו"ח (FK), תאריך גילוי, תאריך החלמה.
4. התחסנות: Vaccination: קוד חיסון (PK), ת.ז. חבר קו"ח (FK), קוד סוג חיסון (FK), תאריך.
5.	סוג החיסון: VaccinationType: קוד חיסון (PK), שם חיסון.
6.	ערים: City: קוד עיר (PK), שם עיר.

הסבר למבנה הטבלאות:
עבור כל חבר קופ"ח נשמר מידע אישי כמו תז, שם ועוד עבורו קיימת הישות Patient. 
כתובת החבר מתפצלת גם כן לעיר רחוב ועוד, מידע זה הרי שימושי לקופ"ח (שליחת הודעות דרך הדואר ועוד). לכן, עבור מידע זה נוצרה הישות Paddress, המשתמשת בישות City.
לשמירת מידע אודות תקופות בהן חבר קופ"ח היה חולה קורונה חיובי נוצרה הישות SicknessPeriod.
לשמירת מידע אודות החיסונים של החבר, קיימת הישות Vaccination, המכילה מידע עבור סוג החיסון בישות VaccinationType.
הטבלאות City וVaccinationType הן טבלאות קוד, בעוד שהטבלאות Patient, SicknessPeriod, Vaccination וPaddress מכילות מידע נוסף.

עבור Patient, בחרתי שלא להשתמש בתעודת הזהות כמפתח ראשי, כי כך מסובך ומסוכן לעדכנו. תעודת זהות דורשת עדכון במקרה של הקלדה שגויה, לפיכך העדפתי להוסיף את העמודה קוד חבר קופ"ח.

לצורך התקנת מסד הנתונים יש להריץ את השאילה המצורפת בקובץ HealthClinic.sql (נוסה הותקן בSQL SERVER).
להלן קישור לקובץ:


**צד שרת:
**צד השרת נכתב ב C#.
צד השרת נוצר בשפת C# במודל 3 השכבות Entity framework. שלב ההתחברות למסד הנתונים הוא די פשוט: הורדות הספריות SQL SERVER, TOOLS והרצת פקודת התחברות לפי שרת, שם מסד נתונים וכו'.
הפקודה אותה הרצתי בתוך ה console של פרויקט ב Class library של DAL:
Scaffold-DbContext "Server= DESKTOP-BRURIAA; Database=HealthClinic; Trusted_Connection=True; TrustServerCertificate=True" Microsoft.EntityFrameworkCore.SqlServer -OutputDir DataBase 

 חלקתי את צד השרת לשכבת DAL בה התבצע חיבור למסד נתונים וגישה ישירה אליו.
  שכבת BLL בה מתרחשות פעולות לוגיות שונות, שכבה זו תלויה בשכבת ה DAL. בנוסף, בשכבה זו יצרתי העתק של מסד הנתונים ללא קשרי גומלין לנוחות המשתמש. לפיכך, הצרכתי להשתמש בממיר AUTO MAPPER ההופך את ישויות מסד הנתונים לישויות החדשות ללא קשרי הגומלין (הצרכתי להוריד AUTO MAPPER). בשכבה זו הוספתי שדות לטבלאות מסוימות כדי שבשליפה אחת לא אצטרך לשלוף טבלאות נוספות (לצורך שימוש במפתח זר), הבאתי את הנתונים הבסיסיים לישויות החדשות (גישה למסד נתונים לוקחת זמן רב). שכבת CONTROLLERS התלויה בDAL ובBLL המתקשרת עם המשתמש ומאזינה לבקשות שרת מסוג GET, POST, PUT DELETE.
בפרויקט כולו נעשה שימוש בהזרקת תלויות: במקום להיות תלויים בפונקציות מסוימות תלויים ביכולת מסוימת. מאפשר גמישות ושינוי בקלות יותר בעתיד. בפרויקט כולו הממשקים גנריים, כך שאין קוד כפול, והוא מתאים לישויות מכל סוג. 

האפשרויות המוצעות בצד השרת:
מכיל CRUD מלא, בדיקות תקינות, 
מלבד עדכון ל City, SicknessPeriod, Vaccination.
עבור סוג חיסון מוצעת אפשרות Get בלבד.

עבור Patient, Vaccination and SicknessPeriod אפשרות המחיקה היא הפיכת הסטטוס שללהם לFalse, וזאת משום שחשוב לשמור מידע זה עבור קופת החולים. עבור שאר הישויות, מחיקה מוחקת את הרשומה ממסד הנתונים ללא יכולת שחזור.

עבור מחיקה Patient נמחק המידע על החיסונים שלו והתקופות בהן היה חולה.

בכל עדכון/ מחיקה בוצעה בדיקה האם האובייקט המבוקש קיים כמובן.

כתובות של החברים בקופת החולים נמצאים בטבלה פרדת בשם Paddress, כדי למנוע רשומות כפולות במקרה שכמה חברי קופ"ח גרים באותו בית עם אותו כתובת. עבור כמה חברים הדרים באותה כתובת- יקבלו את אותו קוד כתובת. 
במחיקת חבר מתבצעת בדיקה האם יש צורך למחוק את רשומת הכתובת או שמא ישנו חבר קופ"ח הרשום על אותה כתובת- ואז לא מתבצעת מחיקה.
בעדכון, נבדק האם יש ליצור רשומה חדשה או לעדכן רשומה קיימת (שוב, בהתאם לכמות החברים הרשומים באותה כתובת).

קבצים מצורפים: קובץ ZIP של כל ה SOLUTION.

**צד לקוח:
**צד הלקוח נעשה ע"י שימוש בספריות ANGULAR.
הניתובים שונו בהתאם לתוכן הComponent, מידע שיש לשתף בין Components השונים ותקשורת עם השרת נמצאים בServices.
כדי שהמידע שימצא אצל הלקוח יהיה המעודכן ביותר, בכל דרישה של תקשורת עם מסד הנתונים בוצעה קריאת שרת נוספת. אם בעתיד יעדיפו מידע פחות מהימן אך קבלה באופן מהיר יותר, אפשר להשתמש במידע שיובא כבר ללא ביצוע קריאות שרת אלו.
עבור טפסים בצד השרת, גם בדקה תקינות הנתונים.

ממשק האתר הינו בשפה האנגלית, העיצוב נעשה בעזרת BOOTCAMP.

האפשרויות באתר:
הדרישות עבור צד הלקוח: להראות מידע אודות החברים, ומידע נוסף עבור כל חבר באופן פרטי, כולל מידע אודות החיסונים שלו והתקופות בהן היה חולה.
אפשרתי אופציות נוספות: Bonus!!
עבור של חבר קופ"ח נשמר מידע אודות כתובת תמונה שלו, והצגתה באתר יחד עם שאר פרטיו האישיים.
יצרתי טופס להוספת חבר קופ"ח חדש, ועדכון.
ההוספה עובדת טוב, אך בעדכון שפיכת הנתוים לטופס לא עובדת כמו שצריך.
כמו כן, מתוך המידע אודות חבר, ניתן להגיע לטופס ולהוסיף תקופה בה היה חולה.
בלחיצה על 'מידע נוסף' ניתן לראות כמה חברי קופ"ח אינם מחוסינם כלל.
(במאמר מוסגר: ננעשה כל מאמץ לשפר את התוצר ולתקן את השגיאות בטווח הזמן הנתון).

בניית מפרט ארכיטקטוני של המערכת: עבור כל ישות בAngular ישנו Service נפרד: עבור Patient יש PatientService וכו'. כל התקשורת עם השרת הAPI נוצרת כאן: הService של Patient מתקשר עם PatientController ושלוח אליו את הבקשות הבאות: Get עבורGetAll(), GetObject(int code)t, Post עבור Add(p:Patient), Put עבור עדכון חבר וDelete עבור מחיקת חבר Delete(int pcode).

להלן צילומי מסך והסבר אודות תהליך השימוש באתר: 
ראשית כאמור, יש לצור את מסד הנתונים (שימוש בשאילתה הנתונה לעיל). יש לפתוח את ה Solution ולהריץ את השרת.
מצורפת תקיה בשם src אותה יש לשתול בספרית Angular ולהריץ את הפקודה המעלה את האתר: ng s -o

מסך ראשוני:
![עמוד הבית](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/55841757-cc1a-4a3a-9706-26343830d17c)
למעלה ממוקם סרגל כלים, לנוחות המשתמש הוא Sticky. 
בלחיצה על Patients יוצג העמוד הבא:
העמוד מכיל הרבה קוביות (Dives), כך שכל קוביה מייצגת חבר קופ"ח אשר הסטטוס שלו חיובי (לא מחוק). 
![בלחיצה על חברי קופח בסרגל הראשי](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/8b3a5d92-e56f-45ab-8a5d-56a500f6d4d3)
להוספת חבר נוסף לקופה, יש ללחוץ על הכפתור "הוספת חבר" שיוביל לפתיחת טופס עבור חבר (נבדקת תקינות קלט). להוספה למסד הנתונים יש לאשר את ההוספה (בתנאי שהנתוינם תקינים) על ידי לחיצה נוספת על כפתור "הוסף". 
![טופס הוספת פציינט](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/3e1e8694-121f-44cf-b9e5-79d80199b358)
בלחיצה על Sickness Periods יוצג העמוד הבא:
כל קוביה מייצגת תקופת חולי של כל החברים בקופת החולים.
![מידע על תקופות חולי](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/8e63f93c-8f02-405d-9e20-306269dd72e4)
בלחיצה על Vaccinations יוצג העמוד הבא:
כל קוביה מייצגת מידע אודות חיסון בודד עבור כל החברים.
![מידע על כל החיסונים](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/5316e139-de77-465e-89d1-7b6d6c12dc6b)
בלחיצה על Information מוצגת כמות החולים בקופת החולים אשר אינם מחוסנים כלל:
![כמות לא מחוסנים](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/3818f184-d3b6-466f-8bc4-1707a63b3d69)
מתוך העמוד של כל אוסף חברי הקופה, לחיצה על חבר מסויים, תוביל לעמוד חדש בו מוצג מידע אישי אודות החבר: פרטים אישיים, (כולל תמונה) וכן מידע אודות החיסונים שלו (אם התחסן) ותקופות בהן היה חולה (אם היה חולה קורונה אי פעם).
![קומפוננט חבר פרטי ](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/76348243-6e93-4729-98f5-2ae2a2826e0d)
מכאן, בלחיצה על הכפתור עדכון חבר, יפתח (בדף זה) טופס לשליחת נתוניו המעודכנים של החבר. לעדכון במסד הנתונים יש ללחוץ על "עדכון". לסגירת הטופס ניתן ללחוץ על "סגור".
![טופס עדכון פציינט](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/0650e6ea-1b73-4e24-bc5a-8cf56ea00fa5)
להוספת מידע על חולי של חבר קופ"ח, נינתן ללחוץ על הכפתור "הוסף תקופת חולי", שינתב לרכיב המכיל טופס הוספת חולי עבור אותו חבר:
![טופס הוספת חולי לפציינט, להגיע דרך פציינט פרטי](https://github.com/BruriaAnaelCohen/Hadasim4/assets/149057415/149d3c21-2bd8-4d8c-b250-7ae7bae8c542)
בכל שלב, לחיצה על האייקון הראשי תוביל לדף הראשי של הקופה.
השימוש באתר מובן, נעים לעין ופשוט. בהצלחה!!

All Rights Reserved to Bruria Anael Cohen

**תרגיל מספר 2:
**
התרגיל מומש בשפת Python בסביבת העבודה PyCharm.
היה אפשר לעשות את התרגיל מונחה עצמים: ליצור מחלקה אבסטרקטית Shape, שממנה יורשים Rectangle וTriangle, אך בסוף החלטתי לוותר על זה וממש את האלגוריתם ללא שימוש בתכנות מונחה עצמים. 
בתוכנית נבדק קלט המשתמש כדי שהתוכנינת לא תפול לעולם. (שוב, גם תרגיל זה ניסיתי לשפר במסגרת הזמן שניתן).

יצרתי אלגוריתם חדש שכן משתמש ב OOP, שמו: Exercise 2 Twitter towwers using OOP updated.py

**תרגיל מספר 3:
**
מפורט בקובץ Docx.


