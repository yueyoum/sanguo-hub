def run():
    from django.core.management import call_command
    f = open('datatable', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        _, fixture = line.split(':')
        fixture = fixture.rstrip('\n')
        try:
            call_command('loaddata', fixture)
        except Exception as e:
            print "ERROR: ", e
            continue

if __name__ == '__main__':
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub.settings')
    run()

