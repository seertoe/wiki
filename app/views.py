from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']
    

    
class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/Panagiotis_Pipinelis/')
    def local_news(self):
        param1 = 'Panagiotis Pipinelis'
        param2 = 'The Greek case was brought to the European Commission of Human Rights in September 1967. It alleged violations of the European Convention on Human Rights (ECHR) by the Greek junta, which had come to power in a coup and launched widespread political repression. A second case alleging additional violations, including of Article 3 forbidding torture, was added in 1968. In 1968 and 1969, a subcommission questioned witnesses and embarked on a fact-finding mission to Greece. Their report proving systematic torture was leaked to the press and turned European public opinion against Greece. On 12 December 1969, the Committee of Ministers of the Council of Europe considered a resolution to expel Greece. To save face, foreign minister Panagiotis Pipinelis (pictured) denounced the ECHR and walked out. Greece returned to the organization after the Greek democratic transition in 1974. The case was influential as a precedent in human rights jurisprudence, especially for the legal definition of torture.'
        param3 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Griekse_minister_van_Buitenlandse_Zaken_Pipinelis_op_Schiphol%2C_links_hr._van_Tie%2C_Bestanddeelnr_921-2580.jpg/172px-Griekse_minister_van_Buitenlandse_Zaken_Pipinelis_op_Schiphol%2C_links_hr._van_Tie%2C_Bestanddeelnr_921-2580.jpg'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1, param2=param2, param3=param3)

    @expose('/Porsche_911/')
    def porsche_911(self):
        param1 = 'Porsche 911'
        param2 = 'The Porsche 911 (pronounced Nine Eleven or in German: Neunelfer) is a two-door 2+2 high performance rear-engined sports car introduced in September 1964 by Porsche AG of Stuttgart, Germany. It has a rear-mounted flat-six engine and a torsion bar suspension. The car has been continuously enhanced through the years but the basic concept has remained unchanged.[1] The engines were air-cooled until the introduction of the 996 series in 1998.[2][3]The 911 has been raced extensively by private and factory teams, in a variety of classes. It is among the most successful competition cars. In the mid-1970s, the naturally aspirated 911 Carrera RSR won world championship races including Targa Florio and the 24 Hours of Daytona. The 911-derived 935 turbo also won the 24 Hours of Le Mans in 1979. Porsche won the World Championship for Makes in 1976, 1977, 1978, and 1979 with 911-derived models.In a 1999 poll to determine the Car of the Century, the 911 was fifth.[4] It is one of two in the top five that had remained continuously in production (the original Beetle remained in production until 2003).[5] The one millionth example was manufactured in May 2017 and is in the company’s permanent collection.[6]'
        param3 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Porsche_911_No_1000000%2C_70_Years_Porsche_Sports_Car%2C_Berlin_%281X7A3888%29.jpg/280px-Porsche_911_No_1000000%2C_70_Years_Porsche_Sports_Car%2C_Berlin_%281X7A3888%29.jpg'
        self.update_redirect()
        return self.render_template('news.html', param1=param1, param2=param2, param3=param3)
    
    @expose('/Porsche_982/')
    def porsche_982(self):
        param1 = 'Porsche 982'
        param2 = "The Porsche 982 is the internal designation of the fourth generation Boxster and third generation Cayman made by German automobile manufacturer Porsche. With the switch to a new turbocharged flat-four engine the marketing name for the models was changed to Porsche 718, in reference to the 718, which won the Targa Florio race in 1959 and 1960. The name is meant to evoke Porsche's past racing successes with light cars like the 718 that outmaneuvered competitors with larger and more powerful engines."
        param3 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Porsche_718_Cayman_GT4_at_IAA_2019_IMG_0257.jpg/280px-Porsche_718_Cayman_GT4_at_IAA_2019_IMG_0257.jpg'
        self.update_redirect()
        return self.render_template('news.html', param1=param1, param2=param2, param3=param3)



db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Panagiotis Pipinelis', category="News")
appbuilder.add_link("Porsche 911", href="/newspageview/Porsche_911/", category="News")
appbuilder.add_link("Porsche 982", href="/newspageview/Porsche_982/", category="News")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

