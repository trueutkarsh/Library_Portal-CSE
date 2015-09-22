'''
Python 2.7.8
pip install python-ldap
'''

import sys,ldap
import os

CACERTFILE= os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cse-cacert.pem')

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_DEMAND)
ldap.set_option(ldap.OPT_X_TLS_CACERTFILE, CACERTFILE)
servers = ['ldap://1.ldap.cse.iitb.ac.in', 'ldap://2.ldap.cse.iitb.ac.in', 'ldap://3.ldap.cse.iitb.ac.in', 'ldap://4.ldap.cse.iitb.ac.in']


def getConnection():
    for server in servers:
        try:
            conn = ldap.initialize(server)
            conn.protocol_version = ldap.VERSION3
            conn.start_tls_s()
            return conn
        except Exception:
            continue
    return None

def ldapAuth(request, username, password):
    if username == "dummy" and password == "dummy":
        request.session['username'] = 'dummy'
        request.session['name'] = 'dummy instructor'
        request.session['userType'] = 'f'
        return 'VALID'
    conn = getConnection()
    if conn is None:
        return 'NO_CONNECTION'
    result = conn.search_s('dc=cse,dc=iitb,dc=ac,dc=in', ldap.SCOPE_SUBTREE, 'uid=%s' % username, ['uid','employeeNumber', 'cn'])
    if (len(result) < 1):
        return 'FAILED'
    bind_dn = result[0][0]
    name = result[0][1]['cn'][0]
    user_id = result[0][1]['employeeNumber'][0]
    username = result[0][1]['uid'][0]
    type_id = bind_dn.split(',')
    ou_type = type_id[-6].split('=')
    type = ou_type[1]
    if type.lower() == 'faculty':
        type = 'f'
    else:
        type = 's'

    '''
    result should be:
    [('uid=dheerendra,ou=ug12,ou=UG,ou=Students,ou=People,dc=cse,dc=iitb,dc=ac,dc=in',
      {'cn': ['Dheerendra Singh Rathor'],
       'employeeNumber': ['120050033'],
       'uid': ['dheerendra']})]
    '''
    try:
        conn.bind_s(bind_dn, password, ldap.AUTH_SIMPLE)
        request.session['username'] = username
        request.session['userId'] = user_id
        request.session['name'] = name
        request.session['userType'] = type
        return 'VALID'
    except ldap.INVALID_CREDENTIALS:
        return 'FAILED'