from flask_restful import Resource, fields, marshal_with
from restfulDemo.controllers.module1 import fields as jf_fields


# String format output of tag
nested_tag_fields = {
    'id': fields.String(),
    'name': fields.String()}

# String format output of post
post_fields = {
    'author': fields.String(attribute=lambda x: x.user.username),
    'title': fields.String(),
    'text': jf_fields.HTMLField(),
    'tags': fields.List(fields.Nested(nested_tag_fields)),
    'publish_date': fields.DateTime(dt_format='iso8601')}


class PostApi(Resource):
    """Restful API of posts resource.>> 实现 PostApi 资源类"""

    @marshal_with(post_fields)
    def get(self, post_id=None):
        """Can be execute when receive HTTP Method `GET`.
           Will be return the Dict object as post_fields.
        """

        if post_id:
            return {'post_id': post_id}
        return {'hello': 'world'}

