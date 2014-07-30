def run():
    import os
    import subprocess
    from django.conf import settings
    fixture_path = settings.FIXTURE_DIRS[0]
    with open('datatable', 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip('\n')
        model, file_name = line.split(":")
        #cmd = 'python manage.py dumpdata {0} --indent=4 > {1}'.format(model, os.path.join(fixture_path, file_name))
        #cmd = ['python', 'manage.py', 'dumpdata', model, '--indent=4', '>', os.path.join(fixture_path, file_name)]
        cmd = ['python', 'manage.py', 'dumpdata', model, '--indent=4']
        print cmd
        stdout = open(os.path.join(fixture_path, file_name), 'w')
        subprocess.Popen(cmd, stdout=stdout)



if __name__ == '__main__':
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub.settings')
    run()
