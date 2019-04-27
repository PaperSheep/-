from django.test import TestCase, Client

from .models import Student


class StudentTestCase(TestCase):
    # 每个测试函数运行时，都会调用一下
    def setUp(self):
        Student.objects.create(
            name = 'PaperSheep',
            sex = 1,
            email = '1009304154@qq.com',
            profession = '兴趣使然',
            qq = '3333',
            phone = '32222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name = 'ziyang',
            sex = 1,
            email = '1009304154@qq.com',
            profession = '兴趣使然',
            qq = '3333',
            phone = '13922064366',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name = 'ziyang',
            sex = 1,
            email = '1009304154@qq.com',
            profession = '兴趣使然',
            qq = '3333',
            phone = '13922064366',
        )
        name = 'PaperSheep'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex = 1,
            email = '333@dd.com',
            profession = '程序员',
            qq = '3333',
            phone = '32222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302~!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain "test_for_post"')

