from bottle import route, run

@route('/on/:out')
def on(comma_outs):
    outs = comma_outs.split(',')
    return {'status':'success'} if validate(outs) else {'status':'error'}

@route('/off/:out')
def off(comma_outs):
    outs = comma_outs.split(',')
    return {'status':'success'} if validate(outs) else {'status':'error'}

def validate(outs):
    try:
        for out in outs:
            int(out)
    except:
         return False
    return True

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)