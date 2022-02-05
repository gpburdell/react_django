class DbRouter:
    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'lndb':
            return 'lndb'
        return 'default'
 
    # def db_for_write(self, model, **hints):
    #     if model._meta.app_label in self.route_app_labels:
    #         return 'default'
    #     return None

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'lndb':
            return None
        return 'default'
 
    def allow_relation(self, obj1, obj2, **hints):
        # We have a fully replicated cluster, so we can allow
        # relationships between objects from different databases
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Only allow migrations on the primary
        return db == 'default'