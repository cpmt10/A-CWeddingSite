from website import create_app
"""
Entrance point of application. When running this Web App run it thorugh here
"""

app = create_app()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

   