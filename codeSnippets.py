

import sys
import os
import time
sys.path.extend(['C:\\MYP\\Python\\pywinauto-0.4.2'])
try:
    from pywinauto.application import Application
    from pywinauto import tests
    from pywinauto.findbestmatch import MatchError
    from pywinauto import findwindows
    from pywinauto import WindowAmbiguousError
    from pywinauto.controls import WrapHandle
    from pywinauto.win32structures import HARDWAREINPUT
    from pywinauto.timings import Timings
except ImportError:
    import os.path
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    import sys
    sys.path.append(pywinauto_path)




sys.path.extend(['C:\\MYP\\Python\\xlrd-0.9.3'])
import xlrd
import shutil
import zipfile


# UTILITY FUNCTI

def Test():
	return 'hello'
def copyDirectory(src, dest):
    sys.stderr.write ( 'Copied Directory '+src+ ' To destination '+dest+'\n')

    copytree_local(src, dest)


def copytree_local(src, dst, symlinks=False, ignore=None):

    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()


    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                shutil.copytree(srcname, dstname, symlinks, ignore)
            else:
                # Will raise a SpecialFileError for unsupported file types
                 shutil.copy2(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files

        except EnvironmentError, why:
            errors.append((srcname, dstname, str(why)))
    try:
         shutil.copystat(src, dst)
    except OSError, why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.append((src, dst, str(why)))
    if errors:
        raise  errors



def cleanDirectory(src):

        #shutil.rmtree(src)
        os.mkdir('C:\a')
        #sys.stderr.write (  'Cleaned Directory '+src+'\n')
        return "cleaned "+src

def writeToFile(src):
    src ='\\\\a\hi.txt'
    if(os.path.exists(src)):
        #os.mkdir(src)
        #sys.stderr.write (  'Cleaned Directory '+src+'\n')
        return "cleaned "+src


def all_subdirs_of(b='.',subDir='a'):
    import re
    result2 = []
    result1= []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        #a = re.compile("^MYP_bc$")
        a = re.compile("^(MYP\-.*?)$")
        m=a.match(d)
        if m :             
            result1.append(d)
            #print bd
    sys.stderr.write (  'identfied the directory '+str(result1) + ' as valid dirs'+'\n')
    return result1


class CustomExe4:
    b ='x'
    f = all_subdirs_of


    def __init__(self):
        var=''
   



    #  getting latest directory
    def findLatestDirectory(self):
        root =  '\\\\abc'
        all_subdirs = all_subdirs_of(root)
        listSub=[]
        for d1 in all_subdirs:
            d1=d1+'\\'+d1+'.zip'
            if(os.path.exists(os.path.join(root,d1))):
                listSub.append(os.path.join(root, d1))

        #print(listSub)
        latest_subdir = max(listSub, key=os.path.getmtime)
        latest_subdir =latest_subdir.rsplit("\\",1)[0]
        sys.stderr.write (  'Got the latests subdir as '+latest_subdir+'\n')
       

        subDirToCopy='QA_Tools\\GenerateMeTestFiles'


        lastSubDirName = latest_subdir.rsplit('\\',1)[1]
        fulldir = latest_subdir+'\\'+lastSubDirName
        fulldir1 = os.path.join(fulldir,subDirToCopy)

        if(os.path.isdir(fulldir)==False):
        #if(1>2):
            #print fulldir+'is not a directory'+' so unziping'
            #print ' WARNING: THE DIRECTORY THREE BUILDS BEFORE THIS WILL BE CLEANED '
            zip = zipfile.ZipFile(fulldir+'.zip')
            #zip.extractall(path=latest_subdir)
            #time.sleep(30000)
        build_nr= int(fulldir.rsplit(".",3)[3])

        dirName= fulldir1.rsplit("\\",2)[1]
        #print(dirName)
        pvsBuild_nr= build_nr-8
        #print('pvs build number is '+str(pvsBuild_nr))
        if(pvsBuild_nr<100):
            pvsBuildnrStr = ''+str(pvsBuild_nr)
        if(build_nr<100):
            buildnrStr = ''+str(build_nr)
        #print str(fulldir)+'is the fulldir'
        fulldir1Pvs = fulldir.replace(str(build_nr),str(pvsBuild_nr))
        sys.stderr.write(fulldir1Pvs+' is to be cleaned')

        return latest_subdir
     
  # USING AUTOIT
    def RunTestTool(self, year, quarter, sleeptime):
      
        Timings.Defaults()
        app = Application()
        try:
            app.connect_(title_re = ".*a.*")
            sys.stderr.write ( 'connected to window '+'\n')
        except:
            import sys, string, os
            app.start_('C:\\MYP\\Python\\start.bat')
            time.sleep(5)
            app.connect_(title_re = ".*a.*")
            sys.stderr.write ( 'connected to window '+'\n')
        app.connect_(title_re = ".*a.*")
      
        app.top_window_().Restore()
        Timings.Fast()
        window = app.window_(process=18000)
        window.SetFocus()
        time.sleep(5)
        app.top_window_().Click()
        time.sleep(5)
        #window.TypeKeys("{TAB 2}")
        window.TypeKeys("{RIGHT 2}")
        window.TypeKeys("{TAB 4}")
        sys.stderr.write ( 'tabbing completed'+'\n')
        dict =  app.top_window_()._ctrl_identifiers()
        print dict
        for k,v  in dict.items():
            #print v
            for v1 in v:
                if (v1==u'a'):
                    print k.handle
                    #k.Click()



        app.top_window_().YearComboxBox.Select(year)


        #app.top_window_().ComboBox7.Select("a")
        app.top_window_()['a'].Click()

        sys.stderr.write ( 'Setting Options and Clicked'+'\n')
       
        print app.top_window_().PopulationComboBox1.ItemTexts()
        measures= []
        measures = app.top_window_().PopulationComboBox1.ItemTexts()
        print measures
        mmap= {

                'a':['b'],
             
            }

        #from collections import OrderedDict
        #mmap1={}
        #mmap1=OrderedDict((mmap[key], True) for key in mmap)
        measures=mmap.keys()
        measures.sort()
        s=''
        s1=''
        dictErrors ={}
        i=0
        previousError=''
        previousSkip=''
        for measure in measures:
            i=i+1
            #if(i==6):
                #break
            print 'using '
            print measure
            indicators=[]
            indicators=mmap[measure]

            if not measure == '': # Change the not operator if you want to run it for all cases in one go.
                app.top_window_().PopulationComboBox1.Select(measure)
                #indicators= app.top_window_().IndicatorComboBox3.ItemTexts()
                for indicator in indicators:
                    if indicator == '':
                        continue
                    app.top_window_().IndicatorComboBox3.Select(indicator)
                    app.top_window_()['Create and Run TestsButton'].Click()
                    #app.top_window_()['Create and Run TestsButton'].Click()
                    #time.sleep(12)

                    while(True):
                        time.sleep(1)
                        times_Run = app.top_window_()['Testing:Edit'].Texts()[0].strip(" ").split()[0]
                        if(times_Run=='00100'):
                            s1=app.top_window_()['Skip Logic ErrorsEdit2'].Texts()[0].strip(" ")
                            s = app.top_window_()['Measure Engine ErrorsEdit2'].Texts()[0].strip(" ")
                            print s
                            print s1
                            break



                #print dictErrors
        sleeptime = 30
        errors=''



        time.sleep(sleeptime)
        sys.stderr.write ( 'Slept for '+str(sleeptime)+'\n')
        #print s+s1

        #s1 = app.top_window_()['Skip Logic ErrorsEdit2'].Texts()[0]
        #s = app.top_window_()['Measure Engine ErrorsEdit2'].Texts()[0]
        print errors
        print dictErrors
        if(errors != '' ):
            raise AssertionError(errors)
            app.start_('C:\\MYP\\Python\\stop.bat')
        print 'reached3'

        #MayNotWork app.kill()
        app.start_('C:\\MYP\\Python\\stop.bat')
        sys.stderr.write ( 'All done')

    # CLASS LEVEL UTILITIES
    def mapAPop(self):
        self.book = xlrd.open_workbook(self.from_this_dir('C:\\MYP\\Python\\custom.xlsx'), formatting_info=False)
        self.sheet = self.book.sheet_by_name('Sheet1')
        listVals = self.sheet.col_values(0,0,100)
        i = 0
        encounteredSpace = False
        dict = {}
        listSubPop=[]
        lastKeyIndex  =0
        for s in listVals:
            s = str(s)
            if s == '':
                encounteredSpace = True
            if encounteredSpace:
                encounteredSpace = False
                dict.update({str(listVals[lastKeyIndex]) : listSubPop })
                listSubPop = []
                lastKeyIndex=i+1
            else:
                listSubPop.append(s)
            i=i+1
        return dict
# opening excel
    def matchXl_dict(self,year):
        self.book = xlrd.open_workbook(self.from_this_dir('C:\\MYP\\Python\\custom.xlsx'), formatting_info=False)
        self.sheet = self.book.sheet_by_name('Sheet1')
        xlval = self.sheet.col_values( 0,0,4)
        Timings.Defaults()
        app = Application()
        try:
            app.connect_(title_re = ".*Skip Logic.*")
        except:
            app.start_('C:\MYP\Swami-KT\MYP_09_00_00_93\QATools\start.bat')
            time.sleep(5)
            app.connect_(title_re = ".*Skip Logic.*")
              Timings.Fast()
        app.top_window_().PrintControlIdentifiers()

        year = app.top_window_()['ComboBox3'].ItemTexts()
        i=0
        for s in xlval:
            xlstrval = str(s)
            lbunicodeval = year [i]
            lbstrval = str(lbunicodeval)
            print lbstrval
            i = i+1
            print xlstrval
            if(lbstrval==xlstrval): print 'true'

    def from_this_dir(self, filename):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

#TEST SCRIPTS




#CGIscripts
#!C:/Python27-32/Python.exe
# -*- coding: UTF-8 -*-

# enable debugging
#import cgitb
#cgitb.enable()
import sys
import cgi
sys.path.insert(0,'C:\MYP\Python\AutoTest_Desktop_1')
sys.path.insert(0,'C:\MYP\Python\pywinauto-0.4.2')
sys.path.insert(0,'C:/Python27-32/Lib')
import Tester
from Tester import PyMongoTest
arguments=cgi.FieldStorage()
measure=arguments.getvalue('Measure')
result=PyMongoTest.findInDb(measure)
print "Content-Type: application/json"
print
print '{"header":"PywinController.function_findLatestDirectory","payload":'+str(result)+'}'



