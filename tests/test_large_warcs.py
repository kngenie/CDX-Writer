#!/usr/bin/env python

import os
import commands
from pipes import quote

warc_dir = os.path.join(os.path.dirname(__file__), 'warcs')

warcs = {
    'YTV-20120204025848-crawl442/YTV-20120204035110-15431.warc.gz':
        '7a891b642febb891a6cf78511dc80a55',
    'WIDE-20120121162724-crawl411/WIDE-20120121174231-03025.warc.gz':
        '53b19ccd106a4f38355c6ebac8b41699',
    'live-20120312105341306-00165-20120312171822397/live-20120312161414739-00234.arc.gz':
        'a23c3ed3fb459cb53089613419eadce5',
    'wb_urls.ia11013.20050517055850-c/wb_urls.ia11013.20050805040525.arc.gz':
        'b4dabcdfc4d2ba3c4ee94d90352176e5', #missing filedesc:// header
    }

if __name__ == '__main__':
    for file, hash in warcs.iteritems():
        out_cdx = os.path.abspath('tmp.cdx')
        assert not os.path.exists(out_cdx)

        warc_file = os.path.join(warc_dir, file)
        assert os.path.exists(warc_file)

        print "processing", warc_file

        # chdir into warc_dir so that name change does not affect output.
        cmd = ('cd {wd}; /usr/bin/time --format=%e {cdx_writer} {file} >{out}'
               .format(wd=quote(warc_dir), cdx_writer='../../cdx_writer.py',
                       file=quote(file), out=out_cdx))

        print "  running", cmd
        status, output = commands.getstatusoutput(cmd)
        assert 0 == status, 'cdx_writer failed with status {}'.format(status)
        print 'time: ', output
        print 'size: ', os.path.getsize(warc_file)

        cmd = 'md5sum tmp.cdx'
        print "  running", cmd
        status, output = commands.getstatusoutput(cmd)
        assert 0 == status

        warc_md5 = output.split()[0]

        assert hash == warc_md5, 'CDX MD5 expected {}, got {}'.format(
            hash, warc_md5)

        os.unlink('tmp.cdx')

    print "exiting without errors!"
