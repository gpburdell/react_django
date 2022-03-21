class DbRouter:
    def db_for_read(self, model, **hints):
        "Point all operations to 'lndb'"
        if model._meta.app_label == 'lndb':
            return 'lndb'
        if model._meta.app_label == 'seismo':
            return 'seismo'
        if model._meta.app_label == 'wjeanalytics':
            return 'wjeanalytics'
        return 'default'
 
    # def db_for_write(self, model, **hints):
    #     if model._meta.app_label in self.route_app_labels:
    #         return 'default'
    #     return None

    def db_for_write(self, model, **hints):
        "write operations only on default 'default'"
        if model._meta.app_label == 'lndb':
            return None
        if model._meta.app_label == 'seismo':
            return None
        if model._meta.app_label == 'wjeanalytics':
            return None
        return 'default'
 
    def allow_relation(self, obj1, obj2, **hints):
        # We have a fully replicated cluster, so we can allow
        # relationships between objects from different databases
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Only allow migrations on the primary
        return db == 'default'