# کار با داده های خط سیر در دیتاست های دنیای واقعی   
امروزه در عصر فوران تکنولوژی روز به روز تحلیل داده ها و دریافت دانش از آنها نقش کلیدی در دنیای ما ایفا میکنند. شاید از زمان ظهور GPS زمان زیادی نگذشته باشد اما اطلاعات غنی این داده ها به شدت در کانون توجه دانشمندان داده قرار گرفته است. یکی از کاربرد های اساسی داده های GPS تشخیص الگوهای هم حرکتی (Trajectory) میباشد. باتوجه به این که این حوزه به شدت نو و در مرز های دانش است ما سعی میکنیم در این مخزن یک فریم ورک ساده برای استخراج این داده ها ارایه کنیم.       

**⚠️ توجه مخزن روزانه درحال آپدیت شدن میباشد و فعلا پایدار نیست**

## فهرست مطالب:   
[1- تعریف مساله با یک مثال عملی در یک دیتاست کوچک آزمایشی]()  
&emsp;&emsp;[1-1- الگوریتم Platoon]()   
&emsp;&emsp;[1-2- الگوریتم Group]()    
&emsp;&emsp;[1-3- الگوریتم Flock]()    
&emsp;&emsp;[1-4- الگوریتم Convoy]()    
&emsp;&emsp;[1-5- الگوریتم Swarm]()    
&emsp;&emsp;[1-5- الگوریتم جامع GCMP]()    
[2- پایپ لاین استخراج داده های هم حرکتی]()   
&emsp;&emsp;[2-1- گسسته سازی زمان دیتاست]()   
&emsp;&emsp;[2-2- استخراج خوشه های هر لحظه زمانی]()       
&emsp;&emsp;&emsp;&emsp;[2-2-1- الگوریتم DBSCAN برای تشخیص خوشه ها]()     
&emsp;&emsp;&emsp;&emsp;[2-2-2- الگوریتم G-index برای تشخیص خوشه ها]()     
&emsp;&emsp;[2-3- الگوریتم TPRPM]()     
[3- مثال ها و استفاده از فریم ورک]()   
&emsp;&emsp;[3-1- کتابخانه های ضروری]()  
&emsp;&emsp;[3-2- ساخت دیتاست برای تست]()   
&emsp;&emsp;[3-3- اجرای الگوریتم TRPM در داده های تست]()   
&emsp;&emsp;[3-4- مقدار دهی پارامتر ها در الگوریتم ها]()  

       
[ضمیمه اول - آموزش کار با داده های جغرافیایی]()    
&emsp;&emsp;[✔️] کتابخانه pandas / geopandas     
&emsp;&emsp;[✔️] کتابخانه shapely     
&emsp;&emsp;[✔️] کتابخانه pysal     
&emsp;&emsp;[✔️] کتابخانه pyproj             
&emsp;&emsp;[✔️] کتابخانه osmnx / pyrosm               
&emsp;&emsp;[✔️] کتابخانه matplotlib (visualization)         
[ضمیمه دوم - آموزش کار با داده های خط سیر]()    
&emsp;&emsp;[✔️] ساختن یک داده سیر از پایه     
&emsp;&emsp;[✔️] تبدیل نقاط به خط     
&emsp;&emsp;[✔️] گرفتن لوکیشن یک داده سیر در یک زمان خاص    
&emsp;&emsp;[✔️] استخراج قسمت هایی از یک داده خط سیر (clipping)    
&emsp;&emsp;[✔️] اشتراک یک خط سیر با یک چندوجهی    
&emsp;&emsp;[✔️] داده AIS    
&emsp;&emsp;[✔️] تبدیل داده های timestamp  به داده های سیر    
&emsp;&emsp;[✔️] نمایش حرارتی سرعت داده های خط سیر    
&emsp;&emsp;[✔️] تحلیل اکتشافی با مکعب زمان فضا (STC)    
&emsp;&emsp;[✔️] تحمیع در داده های خط سیر     
&emsp;&emsp;[✔️] متحرک سازی و کاوش ویژگی های داده های خط سیر به صورت سه بعدی     
