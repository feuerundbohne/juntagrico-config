from django.apps import AppConfig


class MyConfig(AppConfig):
    name = 'feuerundbohne'
    verbose_name = "Feuer&Bohne"

    def ready(self):
        from juntagrico.forms import RegisterMemberForm
        accept_fotos = (' Ich bin damit einverstanden, dass Fotos von mir auf der Internetseite der '
                        'Genossenschaft veröffentlicht werden. Wenn ich das nicht möchte, kontaktiere '
                        'ich Feuer&Bohne per Mail (info@feuerundbohne.ch).')
        RegisterMemberForm.text['accept_with_docs'] += accept_fotos
        RegisterMemberForm.text['accept_wo_docs'] += accept_fotos
