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

"""<style>
    .error {
        color: red;
    }
</style>"""
title = "<h1>Signup</h1>"
table = """<form method='post'>
        <table>
            <tr>
                <td><label for='username'>Username</label></td>
                <td>
                    <input name='username' type='text' value='' required>
                    <span class='error'></span>
                </td>
            </tr>
            <tr>
                <td><label for='password'>Password</label></td>
                <td>
                    <input name='password' type='password' value='' required>
                    <span class='error'></span>
                </td>
            </tr>
            <tr>
                <td><label for='verify'>Verify Password</label></td>
                <td>
                    <input name='verify' type='password' value='' required>
                    <span class='error'></span>
                </td>
            </tr>
            <tr>
                <td><label for='email'>Email (optional)</label></td>
                <td>
                    <input name='email' type='email' value=''>
                    <span class='error'></span>
                </td>
            </tr>
        </table>
        <input type='submit'>
        </form>"""
content=(title+table)

#def valid_username(username):


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(content)

    def post(self):
        username=valid_username(self.request.get('username'))
        password=valid_password(self.request.get('password','verify'))

        if not(username and password):
            self.response.out.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
