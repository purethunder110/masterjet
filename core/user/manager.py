from django.contrib.auth.models import BaseUserManager
import logging

log=logging.getLogger(__name__)

class UserManager(BaseUserManager):
    
    def create_user(
            self,email,username,first_name,password=None,**extra_fields
    ):
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**extra_fields)
        if password:
            user.set_password(password)
        else:
            log.critical(f"The User is beign Created with No password in place!! Email:{email}")
        
        user.save()
        return user
    
    def create_superuser(
            self,email,username,first_name,password=None,**extra_fields
    ):
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,is_staff=True,is_superuser=True,**extra_fields)
        log.info(f"Superuser is created!! Email:{email}")
        if password:
            user.set_password(password)
        else:
            log.critical(f"The User is beign Created with No password in place!! Email:{email}")
        
        user.save()
        return user

    def create_staff(
            self,email,username,first_name,password=None,**extra_fields
    ):
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,is_staff=True,is_superuser=False,**extra_fields)
        log.info(f"A new staff member is beign created!! Email:{email}") 
        
        if password:
            user.set_password(password)
        else:
            log.critical(f"The User is beign Created with No password in place!! Email:{email}")
        
        user.save()
        return user