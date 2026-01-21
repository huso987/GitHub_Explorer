from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.Str()
    avatar_url = fields.Str()
    followers = fields.Int()
    following = fields.Int()
    public_repos = fields.Int()
