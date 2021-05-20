import camelot
import pandas as pd
from pathlib import Path

def pdf_read():
    pfile = input(r"Enter PDF Address")
    table1 = camelot.read_pdf(pfile,pages='1,2,3,4,5,6',shift_text=['r','t'])
    return table1

def time_date_scrapper(table,sec,sub_sec):
    sectd={'Monday':{},'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{}}

    for j in range(6):
        page=j
        for index, rows in tables[page].df.iterrows():
            print('label:', index)
            print('content: \n')
            for i,j in enumerate(rows):
                print(i,j.replace("\n"," "))
                if sec in j:           
                    sectd[tables[page].df.iloc[1,0]][f"Time :{tables[page].df.iloc[2,i]}"]=tables[page].df.iloc[index,i].replace("\n"," ")
                if sub_sec in j:             
                    sectd[tables[page].df.iloc[1,0]][f"Time :{tables[page].df.iloc[2,i]}"]=tables[page].df.iloc[index,i].replace("\n"," ")
    return sectd            
def data_frame_wrangler(datascrap):
    data1=pd.DataFrame(datascrap)
    data2=data1.sort_index()
    data2=data2.fillna("No Class")
    return data2

def main():
    tab=pdf_read()
    isec=input("Enter The Section(in caps)")
    isubsec=input("Enter The Subsection(If Any)")
    scrapped_dict=time_date_scrapper(tab,isec,isubsec)
    final_dataframe=data_frame_wrangler(scrapped_dict)
    print(final_dataframe)

if __name__ == "__main__":
    main()


  

