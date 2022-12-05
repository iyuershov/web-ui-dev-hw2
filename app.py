from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_dashboard():
    user = {
        'first_name': 'Ivan',
        'last_name': 'Ershov',
        'avatar': 'avatar.png',
        'checkouts': 1
    }

    dashboard_data = [
        {
            'title': 'Total users',
            'number': f'{89935:,}',
            'diff': 10.2,
            'percentage': '+1.01%'
        },
        {
            'title': 'Total Products',
            'number': f'{23283.5:,}',
            'diff': 3.1,
            'percentage': '+0.49%'
        },
        {
            'title': 'Total users',
            'number': f'{46827:,}',
            'diff': 2.56,
            'percentage': '-0.91%'
        },
        {
            'title': 'Refunded',
            'number': f'{124854:,}',
            'diff': 7.2,
            'percentage': '+1.51%'
        }
    ]

    orders = [
        {
            'id': '#12594',
            'date': 'Dec 1, 2021',
            'customer': 'Frank Murlo',
            'location': '312 S Wilmette Ave',
            'amount': '$847.69',
            'status': 'new'
        },
        {
            'id': '#12596',
            'date': 'Oct 4, 2022',
            'customer': 'Ivan Ershov',
            'location': '312 S Wilmette Ave',
            'amount': '$6147.00',
            'status': 'delivery'
        },
    ]

    return render_template('index.html', user=user, dashboard_data=dashboard_data, orders=orders)
