from routes.payment_routes import payment
app.register_blueprint(payment)
app.register_blueprint(clerk)