
from fabric.api import sudo, cd, run, settings

def nginx(domain):
    '''
    Create new PHP NGINX server in /etc/nginx/ with web directory at /var/www
    '''

    default_config = '''
    server {{
        server_name {1};
        return 301 $scheme://{0}$request_uri;
    }}

    server {{
        server_name {0};
        root /var/www/{0};
        location / {{
            try_files $uri $uri/ /index.php?$args;
        }}

        access_log /var/log/nginx/{0}.access.log;
        error_log /var/log/nginx/{0}.error.log;

        include /etc/nginx/www_params;
        include /etc/nginx/fastcgi_php;
    }}
    '''
    new_config = default_config.format(domain, domain[4:])

    with cd('/etc/nginx/sites-available/'):
        with settings(warn_only=True):
            if (put(StringIO(new_config), domain)).failed:
                pass

    with cd('/etc/nginx/sites-enabled'):
        with settings(warn_only=True):
            if (run("ln -s /etc/nginx/sites-available/" + domain)).failed:
                pass

    www(domain)

    sudo('invoke-rc.d nginx reload')