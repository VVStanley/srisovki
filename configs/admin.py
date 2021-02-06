from solo.admin import SingletonModelAdmin

from django.contrib import admin

from configs.models import \
    PostConfiguration, HomeConfiguration,\
    ReklamaAll, ReklamaCategory, ReklamaPosts,\
    Metrics, StepDrawingConfiguration,\
    ReklamaStepPosts

admin.site.register(PostConfiguration, SingletonModelAdmin)
admin.site.register(HomeConfiguration, SingletonModelAdmin)
admin.site.register(ReklamaAll, SingletonModelAdmin)
admin.site.register(ReklamaCategory, SingletonModelAdmin)
admin.site.register(ReklamaPosts, SingletonModelAdmin)
admin.site.register(Metrics, SingletonModelAdmin)
admin.site.register(StepDrawingConfiguration, SingletonModelAdmin)
admin.site.register(ReklamaStepPosts, SingletonModelAdmin)
