import os

__author__ = 'davidsiecinski'


class fileReader:
    system_files=[".DS_Store"]

    def prepare_enironment(self, base_path=None):
         # creating  environment at base_path
        data_path=""
        file_path=""
        if base_path==None or base_path=="":
           data_path="data"
        else:
            data_path=base_path+"/data"

        if not os.path.exists(data_path):
            # os.makedirs(data_path)

            learning_path=data_path+"/learning"
            # os.makedirs(learning_path)
            # example author
            author_path=learning_path+"/john_doe"
            os.makedirs(author_path)
            file_path=author_path+"/1.txt"
            try:
                text_file=open(file_path+"", 'w')
                text_file.write("The foreign ministry said a Russian SU-34 jet flew into Turkish airspace on Friday despite warnings.\n Tensions have been high between Ankara and Moscow since Turkey shot down a Russian plane which violated its airspace near Syria in November.\n Russia has been carrying out air strikes in Syria to support government troops near the Turkish border. \n \"A Su-34 plane belonging to the Russian Federation air force violated Turkish airspace at 11:46 local time yesterday (Friday),\" the Turkish foreign ministry said. \n Its statement said the Russian ambassador had been summoned to \"strongly protest and condemn\" the incident.It called the violation a \"concrete indication of Russian acts aiming to escalate problems\" and warned Russia \"will be held responsible for any dire consequences which can emerge from such irresponsible acts\".")
            except IOError as e:
             print "Cannot create example file: "+e.message()

            test_path=data_path+"/test"
            os.makedirs(test_path)
        else:
            raise IOError("path: "+data_path+" already exists")

    def load_all_files_from_dir(self,dir_path):
        list_of_texts=[]
        for filename in os.listdir(dir_path):
            if filename not in self.system_files:
                with open(dir_path+"/"+filename, 'r') as myfile:
                   list_of_texts.append(myfile.read().replace('\n', ''))
        return list_of_texts

    def load_author_files(self,dir_path):
        folders=dir_path.split("/")
        author=folders[len(folders)-1]
        return (author, self.load_all_files_from_dir(dir_path))

    def load_all_data_to_learn(self,dir_path):
        all_data=[]
        if dir_path=="" or dir_path==None:
            dir_path="data/learning"
        else:
            dir_path+="/data/learning"

        if "learning"  in dir_path:
            for filename in os.listdir(dir_path):
                if filename not in self.system_files:
                    all_data.append(self.load_author_files(dir_path+"/"+filename))
        else:
            raise IOError("path: "+dir_path+"in not a  'learning' directory")
        return all_data