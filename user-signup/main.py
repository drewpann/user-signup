#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

V_U = re.compile("^[a-zA-Z0-9_-]{3,20}$")
V_P = re.compile("^.{3,20}$")
V_E = re.compile( "^[\S]+@[\S]+.[\S]+$")

title = "<h1>Signup</h1>"
table = """<form method='post'>
        <table>
            <tr>
                <td><label for='username'>Username</label></td>
                <td>
                    <input name='username' type='text' value='%(username)s' required>
                    <span class='error' style='color:red'>%(nameError)s</span>
                </td>
            </tr>
            <tr>
                <td><label for='password'>Password</label></td>
                <td>
                    <input name='password' type='password' value='' required>
                    <span class='error' style='color:red'>%(passError)s</span>
                </td>
            </tr>
            <tr>
                <td><label for='verify'>Verify Password</label></td>
                <td>
                    <input name='verify' type='password' value='' required>
                    <span class='error' style='color:red'>%(verifyError)s</span>
                </td>
            </tr>
            <tr>
                <td><label for='email'>Email (optional)</label></td>
                <td>
                    <input name='email' type='email' value='%(email)s'>
                    <span class='error' style='color:red'>%(emailError)s</span>
                </td>
            </tr>
        </table>
        <input type='submit'>
        </form>"""
content=(title+table)

def valid_username(username):
    return V_U.match(username)

def valid_password(password):
    return V_P.match(password)

def valid_email(email):
    return V_E.match(email)


class MainHandler(webapp2.RequestHandler):
    def write_content(self,nameError='',passError='',verifyError='',emailError='',username='',email=''):
        self.response.write(content % {'nameError':nameError,'passError':passError,'verifyError':verifyError,
        'emailError':emailError,'username':username,'email':email})

    def get(self):
        self.write_content()

    def post(self):
        username=cgi.escape(self.request.get('username'))
        email=cgi.escape(self.request.get('email'))
        password=cgi.escape(self.request.get('password'))
        verify=cgi.escape(self.request.get('verify'))

        ValidName=valid_username(username)
        ValidPass=valid_password(password)
        if email != "":
            ValidEmail=valid_email(email)
        else:
            ValidEmail=True

        nameError=''
        passError=''
        verifyError=''
        emailError=''
        if not ValidName:
            nameError="That's not a valid user name"
        if not ValidPass:
            passError="That's not a valid password"
        if ValidPass and password!=verify:
            verifyError="The passwords do not match"
        if not ValidEmail:
            emailError="That's not a valid email address"
        self.write_content(nameError,passError,verifyError,emailError,username,email)

        if ValidName and ValidPass and ValidEmail and password==verify:
            self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome = "<h1>Welcome, %(username)s!</h1>"
        self.response.write(welcome % {'username':username})

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
