from utils import *
from DL_ClassifierModel import *
from args import *
from tool import *
from tool import mkdir

def train(args,log):
    dataClass = DataClass_normal(dataPath='TLR4.csv',
                                 pSeqMaxLen=1024, dSeqMaxLen=128,
                                 sep=' ')
    model = AIGO_DTI(args=args,log=log,cSize=dataClass.pContFeat.shape[1])
    res = model.train(dataClass, args=args,stopRounds=-1,log=log,
            savePath='AIGO-DTI', metrics="AUC", report=["ACC", "AUC", "LOSS",'F1','Precision','AUPR'],
            preheat=0)
    return res

if __name__ == '__main__':
    args = set_train_argument()
    log = set_log('train', args.log_path)
    train(args,log)
