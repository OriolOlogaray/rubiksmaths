using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PiecePosition : MonoBehaviour
{
    public GameObject Cube;
    public GameObject W;
    public GameObject RED;
    public GameObject G;
    public GameObject Y;
    public GameObject O;
    public GameObject BLUE;
    public GameObject WGR;
    public GameObject WR;
    public GameObject WBR;
    public GameObject GR;
    public GameObject BR;
    public GameObject YGR;
    public GameObject YR;
    public GameObject YBR;
    public GameObject WBO;
    public GameObject WO;
    public GameObject WGO;
    public GameObject BO;
    public GameObject GO;
    public GameObject YBO;
    public GameObject YO;
    public GameObject YGO;
    public GameObject WG;
    public GameObject YG;
    public GameObject WB;
    public GameObject YB;
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject F2;
    public GameObject F8;
    public GameObject B2;
    public GameObject B8;
    public GameObject U;
    public GameObject R;
    public GameObject F;
    public GameObject D;
    public GameObject L;
    public GameObject B;
    public static bool prime_pressed = false;
    
    

    // Start is called before the first frame update
    void Start()
    {
        WGR.transform.parent = R1.transform;
        WR.transform.parent = R2.transform;
        WBR.transform.parent = R3.transform;
        GR.transform.parent = R4.transform;
        BR.transform.parent = R6.transform;
        YGR.transform.parent = R7.transform;
        YR.transform.parent = R8.transform;
        YBR.transform.parent = R9.transform;
        WBO.transform.parent = L1.transform;
        WO.transform.parent = L2.transform;
        WGO.transform.parent = L3.transform;
        BO.transform.parent = L4.transform;
        GO.transform.parent = L6.transform;
        YBO.transform.parent = L7.transform;
        YO.transform.parent = L8.transform;
        YGO.transform.parent = L9.transform;
        WG.transform.parent = F2.transform;
        YG.transform.parent = F8.transform;
        WB.transform.parent = B2.transform;
        YB.transform.parent = B8.transform;
        W.transform.parent = U.transform;
        RED.transform.parent = R.transform;
        G.transform.parent = F.transform;
        Y.transform.parent = D.transform;
        O.transform.parent = L.transform;
        BLUE.transform.parent = B.transform;
        R1.transform.parent = Cube.transform;
        R2.transform.parent = Cube.transform;
        R3.transform.parent = Cube.transform;
        R4.transform.parent = Cube.transform;
        R6.transform.parent = Cube.transform;
        R7.transform.parent = Cube.transform;
        R8.transform.parent = Cube.transform;
        R9.transform.parent = Cube.transform;
        L1.transform.parent = Cube.transform;
        L2.transform.parent = Cube.transform;
        L3.transform.parent = Cube.transform;
        L4.transform.parent = Cube.transform;
        L6.transform.parent = Cube.transform;
        L7.transform.parent = Cube.transform;
        L8.transform.parent = Cube.transform;
        L9.transform.parent = Cube.transform;
        F2.transform.parent = Cube.transform;
        F8.transform.parent = Cube.transform;
        B2.transform.parent = Cube.transform;
        B8.transform.parent = Cube.transform;
        U.transform.parent = Cube.transform;
        R.transform.parent = Cube.transform;
        F.transform.parent = Cube.transform;
        D.transform.parent = Cube.transform;
        L.transform.parent = Cube.transform;
        B.transform.parent = Cube.transform;
        for (int i = 0; i < 20; i++)
        {
            if (Cube.transform.GetChild(i).childCount == 3)
            {
                for (int j = 0; j < 2; j++)
                {
                    Cube.transform.GetChild(i).GetChild(Cube.transform.GetChild(i).childCount - 1).GetChild(0).parent = Cube.transform.GetChild(i).GetChild(j);
                }             
            }
            if (Cube.transform.GetChild(i).childCount == 4)
            {
                for (int j = 0; j < 3; j++)
                {
                    Cube.transform.GetChild(i).GetChild(Cube.transform.GetChild(i).childCount - 1).GetChild(0).parent = Cube.transform.GetChild(i).GetChild(j);
                }
            }
        }
    }
}

