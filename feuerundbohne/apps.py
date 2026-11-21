from django.apps import AppConfig


class MyConfig(AppConfig):
    name = 'feuerundbohne'
    verbose_name = "Feuer&Bohne"

    def ready(self):
        from django.forms import BooleanField
        from juntagrico.forms import RegisterMemberForm
        accept_fotos = (' Ich bin damit einverstanden, dass Fotos von mir auf der Internetseite der '
                        'Genossenschaft veröffentlicht werden. Wenn ich das nicht möchte, kontaktiere '
                        'ich Feuer&Bohne per Mail (info@feuerundbohne.ch).')
        original_init = RegisterMemberForm.__init__
        def custom_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.field['accept_fotos'] = BooleanFields(required=True, label=accept_fotos)
            self.helper.layout.insert(-1, 'accept_fotos')
        RegisterMemberForm.__init__ = custom_init
 #       RegisterMemberForm.text['accept_fotos'] += accept_fotos
        
        #RegisterMemberForm.text['accept_with_docs'] += accept_fotos
        #RegisterMemberForm.text['accept_wo_docs'] += accept_fotos
#        try:
#            RegisterMemberForm.text['accept_with_docs'] += accept_fotos
#            RegisterMemberForm.text['accept_wo_docs'] += accept_fotos
#        except Exception as e:
#            pass
            #raise ValueError(f"exception: {e} - debug: {RegisterMemberForm.text}")
