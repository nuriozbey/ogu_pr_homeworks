# OGU Pattern Recognition Homeworks
OGU PR Homework Solutions


### Quiz-2
quiz 2 data.xls dosyası https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
adresinden indirilmiş olup üzerinde düzenleme yapılmıştır. Excel de 3 adet sayfa bulunmaktadır. Sayfalardan biri orijinal veri setini göstermektedir. 
Bu veri setinden bazı sütunlar seçilerek train ve test setleri (diğer 2 sayfada) oluşturulmuştur.
Test ve train setindeki her bir satır bir hastaya ait verileri göstermektedir. Test setindeki her bir hasta için ilk 5 sütündaki verileri
(location, gender, age,	visiting Wuhan,	from Wuhan)  kullanarak kNN sınıflandırıcısı ile
sınıflandırarak hastanın ölüp ölmediğini belirleyerek 6 numaralı sütuna (death_estimation value), train setteki en benzer index numaralarını ise 7 numaralı (knn_index)
yazınız. İstediğiniz programlama dili ile kullanabilirsiniz. 
Exceldeki verileri kullandığınız dile uygun olarak sabit değişken olarak atayabilirsiniz. 

*hyper parametreler:*  
**k = 3**
**distance = L2 (euclidean)**


### Quiz-3
quiz 3 için quiz 2 deki veriler kullanılacaktır.
quiz 2 de knn kullanarak test verilerindeki değerlere göre ölümler tahmin edilmeye çalışılmıştır.
quiz 3 de ise bayes kuralı ile test verisinde verilen değerleri ölümleri tahmin ediniz.
örneğin:
test verisindeki ilk satır olan
location gender age visiting Wuhan from Wuhan
Beijing female 33 0 1
adlı kişinin ölme olasılığını bayes kullanarak bulunuz.

*NOT: eğer olasılık 0.5 üzerinde ise öleceğini altında ise yaşayacağını söyleyebilirsiniz.*


### Quiz-4
Aşağıda verilen 6 elamanı 4 özelliği olan 2 sınıfın birbirinden linear olarak ayrılıp ayrılamadığını bulunuz.

*NOT: covariance matrisini kullanabilirsiniz*


         [ -10 10  2  4 ]         [ -6   8  -7 -4 ]
    X1 = [  -4 -1  2 -6 ]    X2 = [ -6  10  -7 -9 ]
         [   5 -8  2 -1 ]         [  3  10  -2 -9 ]
         [   5  4 10  1 ]         [  8   3  -6 -2 ]
         [   8 -7  9 -3 ]         [ -4  -4 -10 -7 ]
         [  -2 -5  5  2 ]         [ -9  -4   4  2 ]


### Quiz-5
aşağıda verien 6x4 boyutlarındaki matrisi herhangi bir yöntemle 6x2 boyutlarına indiriniz.

*NOT: Matrisin seyrek olduğunu unutmayınız.*

         [   9 -7	 6 9 ]    
    X1 = [  10  0      1 ]    
         [     -3   1  5 ]     
         [  -7      4  9 ]       
         [  -4  5  -7  2 ]        
         [   5  8  -5 -8 ]         


### Quiz-6
2 sınıfı birbirinden ayırmak için gereken support vektörleri ve hyper plane bulunuz.

         [ 3  1 ]         [  1  0 ]
    X1 = [ 3 -1 ]    X2 = [  0  1 ]
         [ 6  1 ]         [  0 -1 ]
         [ 6 -1 ]         [ -1  0 ]
         
