public class SomeService {
    public void saveData(DataToSave dataS, String param) {
        DataA dataA = repoA.find(param);
        if(!judgeA(dataS, dataA)) {
            return;
        }
        DataB dataB = repoB.find(param, dataA.getValue1());
        dataS.valueX = calcValueX(dataS, dataB);
        repoS.save(dataS);
    }
}
