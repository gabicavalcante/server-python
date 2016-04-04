def reboot(port):
    def decorator(f):
        import re
        import commands
        s = commands.getoutput('lsof -i :5000')
        try:
            p_id = re.findall('.*?Python\s+[0-9]{4,7}', s)[0].split(' ')[-1]
        except IndexError:
            p_id = None
        p_id = int(p_id) if p_id else None
        if p_id:
            commands.getoutput('kill -9 {}'.format(p_id))
        return f
    return decorator