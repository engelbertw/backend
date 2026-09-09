● Bash(cat << 'EOF'
  # SPDX-License-Identifier: MPL-2.0
  # Copyright (C) 2019 - 2021 Gemeente Amsterdam
  from django.conf import settings


  def settings_in_context(request):
      return {
          'FEATURE_FLAGS': settings.FEATURE_FLAGS,
          'ORGANIZATION_NAME': settings.ORGANIZATION_NAME,
          'OIDC_RP_CLIENT_ID': settings.OIDC_RP_CLIENT_ID,
          # Zonder deze regel wordt de {% if ADMIN_ENABLE_LOCAL_LOGIN %}-check in
          # admin/login.html nooit True (de instelling bestaat wel en werkt correct
          # voor AUTHENTICATION_BACKENDS, maar werd nooit aan de template doorgegeven)
          # — het loginformulier bleef dan altijd onzichtbaar, ook met de instelling aan.
          'ADMIN_ENABLE_LOCAL_LOGIN': settings.ADMIN_ENABLE_LOCAL_LOGIN,
      }
  EOF)
  ⎿  # SPDX-License-Identifier: MPL-2.0
     # Copyright (C) 2019 - 2021 Gemeente Amsterdam
     from django.conf import settings


     def settings_in_context(request):
         return {
             'FEATURE_FLAGS': settings.FEATURE_FLAGS,
             'ORGANIZATION_NAME': settings.ORGANIZATION_NAME,
             'OIDC_RP_CLIENT_ID': settings.OIDC_RP_CLIENT_ID,
             # Zonder deze regel wordt de {% if ADMIN_ENABLE_LOCAL_LOGIN %}-check in
             # admin/login.html nooit True (de instelling bestaat wel en werkt correct
             # voor AUTHENTICATION_BACKENDS, maar werd nooit aan de template doorgegeven)
             # — het loginformulier bleef dan altijd onzichtbaar, ook met de instelling aan.
             'ADMIN_ENABLE_LOCAL_LOGIN': settings.ADMIN_ENABLE_LOCAL_LOGIN,
         }
