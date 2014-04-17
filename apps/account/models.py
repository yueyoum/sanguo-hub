from django.db import models

class BaseAccountManager(models.Manager):
    def create(self, tp, **kwargs):
        if 'account_id' not in kwargs:
            account = Account.objects.create(tp=tp)
            kwargs['account_id'] = account.id
        return super(BaseAccountManager, self).create(**kwargs)

class AnonymousManager(BaseAccountManager):
    def create(self, **kwargs):
        return super(AnonymousManager, self).create('anonymous', **kwargs)

class RegularManager(BaseAccountManager):
    def create(self, **kwargs):
        return super(RegularManager, self).create('regular', **kwargs)


class ThirdManager(BaseAccountManager):
    def create(self, **kwargs):
        return super(ThirdManager, self).create('third', **kwargs)


class Account(models.Model):
    tp = models.CharField(db_index=True, max_length=32)

    register_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, db_index=True)
    last_server_id = models.IntegerField(default=0)
    all_server_ids = models.CharField(max_length=255, blank=True)
    login_times = models.IntegerField(default=0)

    class Meta:
        db_table = 'account'

    def save(self, *args, **kwargs):
        if not self.login_times:
            self.login_times = 1
        else:
            self.login_times += 1

        if len(self.all_server_ids) < 253:
            all_server_ids = self.all_server_ids.split(',')
            if self.last_server_id and str(self.last_server_id) not in all_server_ids:
                all_server_ids.append(str(self.last_server_id))
                self.all_server_ids = ','.join(all_server_ids)

        super(Account, self).save(*args, **kwargs)


class AccountAnonymous(models.Model):
    token = models.CharField(unique=True, max_length=255)
    account = models.OneToOneField(Account, related_name='info_anonymous')

    objects = AnonymousManager()

    class Meta:
        db_table = 'account_anonymous'


class AccountRegular(models.Model):
    name = models.CharField(unique=True, max_length=255)
    passwd = models.CharField(max_length=255)
    account = models.OneToOneField(Account, related_name='info_regular')

    objects = RegularManager()

    class Meta:
        db_table = 'account_regular'


class AccountThird(models.Model):
    platform = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    account = models.OneToOneField(Account, related_name='info_third')

    objects = ThirdManager()

    class Meta:
        db_table = 'account_third'
        unique_together = (('platform', 'uid'),)



#######################################

class AccountBan(models.Model):
    account = models.OneToOneField(Account)
    reason = models.CharField(max_length=255, blank=True)
    ban_at = models.DateTimeField(auto_now_add=True)
    ban_by = models.ForeignKey('auth.User')

    # recover after ? days. 0 means no auto recover
    recover_after = models.IntegerField(default=0)

    class Meta:
        db_table = 'account_ban'

class AccountBanHistory(models.Model):
    account = models.ForeignKey(Account)
    reason = models.CharField(max_length=255, blank=True)
    ban_at = models.DateTimeField()
    ban_by = models.ForeignKey('auth.User', related_name='ban_history')

    recover_after = models.IntegerField(default=0)
    recover_by = models.ForeignKey('auth.User', related_name='recover_history')


    class Meta:
        db_table = 'account_ban_history'


