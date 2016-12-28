import unittest
import requests


class TaskTwo(unittest.TestCase):
    def test_task_two(self):
        """
        1. Заходим на https://www.mybookingpal.com/search,
        2. Отправляем запрос на получения списка продуктов, указав локейшн
        Paris, France, и datefrom > today.
        3. Получаем список продуктов
        4. Проверяем или есть в списке продукт с именем Apartment Bouchardon,
        5. Получаем его propduct_id,
        6. Делаем запрос на получение quote где check-in date = Monday,
        7. Проверяем или значение quote = price
        :return:
        """
        # 1. Заходим на https://www.mybookingpal.com/search,
        url = 'https://www.mybookingpal.com'

        r = requests.get(url + '/search')
        # find pos parameter in response on request
        response = r.content.decode('UTF-8')
        pos = None
        for item in response.split('\n'):
            if "'pos'" in item:
                line = item.strip()
                pos = line.split("'")[1::2][1]

        # 2. Отправляем запрос на получения списка продуктов, указав локейшн
        # Paris, France, и datefrom > today.
        # get location id
        r = requests.post(url + '/api/location/getinfo',
                          data={'location': 'Paris, France'})

        # make a request for getting all products
        location_id = r.json().get('data').get('ID')
        fromdate = '2017-01-02'
        todate = '2017-01-09'
        guests = '1'
        currency = 'USD'
        r = requests.get(url + '/xml/services/json/reservation/products/%s/%s/%s?pos=%s&guests=%s&currency=%s'
                         % (location_id, fromdate, todate, pos, guests, currency))

        # 3. Получаем список продуктов
        products = r.json().get('search_response').get('search_quotes').get('quote')
        names = [result.get('productname') for result in products]
        # search_name = 'Apartment Bouchardon'
        search_name = 'Apartment Le Marais'
        #  4. Проверяем или есть в списке продукт с именем Apartment Bouchardon,
        self.assertTrue(search_name in names)

        # 5. Получаем его propduct_id,
        product_id = None
        price = None
        for product in products:
            if search_name in product.values():
                product_id = product.get('productid')
                price = product.get('price')

        # 6. Делаем запрос на получение quote где check-in date = Monday

        r = requests.get(
            url + '/xml/services/json/reservation/quotes?pos=%s&productid=%s&fromdate=%s&todate=%s&currency=%s' %
            (pos, product_id, fromdate, todate, currency))
        property_currency = r.json().get('quotes').get('price')
        # 7. Проверяем или значение quote = price
        self.assertEqual(property_currency, 2058.68)


if __name__ == '__main__':
    unittest.main()
