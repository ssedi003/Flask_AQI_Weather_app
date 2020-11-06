from AQI_WebApp_Flask import app, forms
from flask import request, render_template

@app.route('/', methods=['GET','POST'])
def search():
    searchForm = forms.AQIParameters(request.form)
    if request.method=="POST":
        aqiparameter = request.form['aqiparameter']
        parameter_requested = forms.aqi_parameter(aqiparameter)
        # parameter_requested = parameter_requested[aqiparameter]
        
        '''
        If the user makes a post request, please save the selected value by the user into a variable
        Also, call the function aqi_parameter (from forms.py) with all the results
        Then, render template parameter_result.html only with the parameter requested by the user
        Which means that you should assign the correct value for the variable parameter_requested below
        '''

        return render_template('parameter_result.html', result=parameter_requested)
    return render_template('parameter_search.html', form=searchForm)