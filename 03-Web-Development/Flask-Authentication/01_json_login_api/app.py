from flask import Flask ,render_template,request,flash,redirect,url_for ,jsonify,session

app = Flask(__name__)
app.secret_key='my-secret_key'

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        request_data=request.get_json()
        if request_data is None:
            pass
        username = request_data.get('userName')
        password = request_data.get('password')
        
        if not username:
           flash('Name can not be empty','error')
           return redirect(url_for('home'))   
        elif not password:
            flash('password can not be empty','error')
            return redirect(url_for('home')) 
        
        
        if username == 'Admin' and password=='Admin@1234':
           
             session['user_name'] = username

        #    data = {
        #        "status": "success", "message": "Logged in successfully",'data' : username }
           
             return jsonify({
            "status": "success",
            "message": "Logged in successfully",
            "redirect_url": "/welcome",
             'data' : username # Send redirect URL to JS
        }) ,200
        #    
        else:
            return jsonify({
                        "status": "Error",
                        "message": "Invalid Credentials",
                        "redirect_url": "/home"
                      
                    }) ,401
          
    return render_template('home.html')

@app.route('/welcome')
def welcome():
  if 'user_name' in session:
   
      return render_template('welcome.html')
  return redirect(url_for('home'))


@app.route('/api/user/profile', methods=['GET'])
def get_profile_api():
    user_name = session.get('user_name')
    if user_name:
        return jsonify({
            "status": "success",
            "userName": user_name
        }), 200
    return jsonify({"status": "error", "message": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(debug=True)