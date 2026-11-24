import allure

@allure.feature('Создание рецепта')
class TestRecipe:
    @allure.title('После создания рецепта открывается его карточка с заданным названием')
    def test_create_recipe_opens_its_card(self, authorized_header, recipe_form_page, recipe_details_page, recipe_data):
        authorized_header.open_recipe_form()
        recipe_form_page.create(recipe_data)

        assert recipe_details_page.is_open(), 'После создания должна отображаться карточка рецепта'
        assert recipe_details_page.get_name() == recipe_data.name, 'Название в карточке должно совпадать с введённым'
