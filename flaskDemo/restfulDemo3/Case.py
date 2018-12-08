from restfulDemo3.app import db


class Case(db.Model):
    """用例实体表t_case"""
    __tablename__ = 't_case'

    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)   # 主键id
    name = db.Column(db.String(255))                        # 用例标题
    desc = db.Column(db.String(255))                        # 用例描述description
    interface_id = db.Column(db.Integer)                    # 主测接口id
    interface_class_id = db.Column(db.Integer)              # 接口归属的分类id
    project_id = db.Column(db.Integer)                      # 接口归属的项目id
    create_person = db.Column(db.Integer)                   # 用例创建人(user_id)
    create_time = db.Column(db.String(255))                 # 用例创建时间
    update_time = db.Column(db.String(255))                 # 用例最后更新时间

    def __init__(self, case_id=None, name="", desc="", interface_id=None, interface_class_id=None, project_id=None,
                 create_person=None, create_time=None, update_time=None):
        """
        :rtype: db.Model
        """
        self.case_id = case_id
        self.name = name
        self.desc = desc
        self.interface_id = interface_id
        self.interface_class_id = interface_class_id
        self.project_id = project_id
        self.create_person = create_person
        self.create_time = create_time
        self.update_time = update_time

    # def __repr__(self):
    #     return u'<Case case_id=%d name=%s desc=%r>' % (self.case_id, self.name, self.desc)


