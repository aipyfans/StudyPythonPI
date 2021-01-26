import unittest
from app import create_app, db
from app.model import User, Post, Category
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class SQLAlchemyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # 添加默认数据
        admin = User('admin', 'admin@example.com')
        db.session.add(admin)
        peter = User('peter', 'peter@example.com')
        db.session.add(peter)
        guest = User('guest', 'guest@example.com')
        db.session.add(guest)
        db.session.commit()

    def test_query(self):
        # 通过用户名查询用户:
        peter = User.query.filter_by(username='peter').first()
        print('通过用户名查询用户', peter)
        self.assertEqual(peter.username, 'peter')
        self.assertEqual(peter.email, 'peter@example.com')

        missing = User.query.filter_by(username='missing').first()
        self.assertEqual(missing, None)

        # 使用更复杂的表达式查询一些用户:
        list = User.query.filter(User.email.endswith('@example.com')).all()
        print('使用更复杂的表达式查询一些用户', list)
        self.assertEqual(len(list), 3)

        # 按某种规则对用户排序:
        user = User.query.order_by(User.username).first()
        print('按某种规则对用户排序', user)
        self.assertEqual(user.username, 'admin')

        # 限制返回用户的数量:
        list = User.query.limit(1).all()
        print('限制返回用户的数量', list)
        self.assertEqual(len(list), 1)

        # 用主键查询用户:
        user = User.query.get(1)
        print('用主键查询用户', user)
        self.assertEqual(user.username, 'admin')

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()
