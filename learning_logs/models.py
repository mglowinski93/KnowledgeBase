from django.db import models

# Create your models here.
'''
Klasa Topic reprezentuje jeden artykul.
Klasa Topic dziedziczy po klasie models.Model.
models.Model oferuje podstawowa funkcjonalnosc modeli w Django

'''
class Topic(models.Model):
    text = models.CharField(max_length=50) #miejsce do wprowadzenia tekstu. Konieczne jest okreslenie maksylamej dlugosci
    date_added = models.DateTimeField(auto_now_add=True) # pole do przechowywania daty i godziny. Parametr auto_now_add automatycznie przypisuje artykulowi bierzaca godzine poczas tworzenia

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    '''
    Klucz zewnetrzny to zapis z bazdy danych, oznaczajacy odwolanie do innego rekordu w bazie danych
    W omawianym przykladzie jest to polecenie laczace wpis z tematem
    Kazdemu utworzonemu tematowi zostal przypisany klucz (identyfikator)
    Kiedy Django tworzy polaczenia miedzy miedzy dwoma fragmentami danych, wowcza wykorzystuje klucze
    '''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, default = "Title")
    text = models.TextField()#Pole do wpisywania teksu nieograniczone 
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    '''
    Klasa Meta przechowywuje informacje dodatkowe przydatne podczas zarzadzania medelem
    '''
    class Meta:
        verbose_name_plural = 'entries'#Nazwa wyswietlana w panelu administratora
        
    def __str__(self):
        return self.title