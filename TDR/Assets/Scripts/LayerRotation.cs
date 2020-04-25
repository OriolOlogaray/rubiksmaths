using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class LayerRotation : MonoBehaviour
{/*
    public GameObject Cube2;
    public GameObject Cube;
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject U1;
    public GameObject U2;
    public GameObject U3;
    public GameObject U4;
    public GameObject U;
    public GameObject U6;
    public GameObject U7;
    public GameObject U8;
    public GameObject U9;
    public GameObject F1;
    public GameObject F2;
    public GameObject F3;
    public GameObject F4;
    public GameObject F;
    public GameObject F6;
    public GameObject F7;
    public GameObject F8;
    public GameObject F9;
    public GameObject D1;
    public GameObject D2;
    public GameObject D3;
    public GameObject D4;
    public GameObject D;
    public GameObject D6;
    public GameObject D7;
    public GameObject D8;
    public GameObject D9;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject B1;
    public GameObject B2;
    public GameObject B3;
    public GameObject B4;
    public GameObject B;
    public GameObject B6;
    public GameObject B7;
    public GameObject B8;
    public GameObject B9;*/
    public GameObject[] ufrom;
    public GameObject[] uto;
    public GameObject[] uprimeto;
    public GameObject[] rfrom;
    public GameObject[] rto;
    public GameObject[] rprimeto;
    public GameObject[] ffrom;
    public GameObject[] fto;
    public GameObject[] fprimeto;
    public GameObject[] efrom;
    public GameObject[] eto;
    public GameObject[] eprimeto;
    public GameObject[] dfrom;
    public GameObject[] dto;
    public GameObject[] dprimeto;
    public GameObject[] mfrom;
    public GameObject[] mto;
    public GameObject[] mprimeto;
    public GameObject[] sfrom;
    public GameObject[] sto;
    public GameObject[] sprimeto;
    public GameObject[] bfrom;
    public GameObject[] bto;
    public GameObject[] bprimeto;
    public GameObject[] lfrom;
    public GameObject[] lto;
    public GameObject[] lprimeto;/*
    public float speed;
    public string scramblestr;
    public string[] scramblelist;
    private CubeRotations cubeRotations;
    void Awake()
    {
        cubeRotations = Cube2.GetComponent<CubeRotations>();
    }
    public void ymove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {

            Cube2.transform.parent = Cube.transform;
            Cube.transform.Rotate(0, speed, 0 * Time.deltaTime);
            if (Mathf.Abs(Cube.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.y) < 91.5)
            {
                hasrotated = true;
                Cube.transform.rotation = Quaternion.Euler(0, 90, 0);               
                u();
                eprime();
                dprime();
                cubeRotations.reset();
                Cube2.transform.parent = null;
                Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                keypressed = false;
            }
        }
    }
    public void yprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {

            Cube2.transform.parent = Cube.transform;
            Cube.transform.Rotate(0, -speed, 0 * Time.deltaTime);
            if (Mathf.Abs(Cube.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.y) < 271.5)
            {
                hasrotated = true;
                Cube.transform.rotation = Quaternion.Euler(0, -90, 0);
                uprime();
                e();
                d();
                cubeRotations.reset();
                Cube2.transform.parent = null;
                Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                keypressed = false;
            }
        }
    }
    public void rmove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            R1.transform.parent = R.transform;
            R2.transform.parent = R.transform;
            R3.transform.parent = R.transform;
            R4.transform.parent = R.transform;
            R6.transform.parent = R.transform;
            R7.transform.parent = R.transform;
            R8.transform.parent = R.transform;
            R9.transform.parent = R.transform;
            R.transform.Rotate(speed, 0, 0 * Time.deltaTime);
            if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 91.5)
            {
                hasrotated = true;
                R.transform.rotation = Quaternion.Euler(90, 0, 0);
                R1.transform.parent = Cube2.transform;
                R2.transform.parent = Cube2.transform;
                R3.transform.parent = Cube2.transform;
                R4.transform.parent = Cube2.transform;
                R6.transform.parent = Cube2.transform;
                R7.transform.parent = Cube2.transform;
                R8.transform.parent = Cube2.transform;
                R9.transform.parent = Cube2.transform;
                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                r();
                keypressed = false;
            }
        }
    }
    public void rprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            R1.transform.parent = R.transform;
            R2.transform.parent = R.transform;
            R3.transform.parent = R.transform;
            R4.transform.parent = R.transform;
            R6.transform.parent = R.transform;
            R7.transform.parent = R.transform;
            R8.transform.parent = R.transform;
            R9.transform.parent = R.transform;
            R.transform.Rotate(-speed, 0, 0 * Time.deltaTime);
            if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 271.5)
            {
                hasrotated = true;
                R.transform.rotation = Quaternion.Euler(-90, 0, 0);
                R1.transform.parent = Cube2.transform;
                R2.transform.parent = Cube2.transform;
                R3.transform.parent = Cube2.transform;
                R4.transform.parent = Cube2.transform;
                R6.transform.parent = Cube2.transform;
                R7.transform.parent = Cube2.transform;
                R8.transform.parent = Cube2.transform;
                R9.transform.parent = Cube2.transform;
                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                rprime();
                keypressed = false;
            }
        }
    }
    public void umove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            U1.transform.parent = U.transform;
            U2.transform.parent = U.transform;
            U3.transform.parent = U.transform;
            U4.transform.parent = U.transform;
            U6.transform.parent = U.transform;
            U7.transform.parent = U.transform;
            U8.transform.parent = U.transform;
            U9.transform.parent = U.transform;
            U.transform.Rotate(0, speed, 0 * Time.deltaTime);
            if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 91.5)
            {
                hasrotated = true;
                U.transform.rotation = Quaternion.Euler(0, 90, 0);
                U1.transform.parent = Cube2.transform;
                U2.transform.parent = Cube2.transform;
                U3.transform.parent = Cube2.transform;
                U4.transform.parent = Cube2.transform;
                U6.transform.parent = Cube2.transform;
                U7.transform.parent = Cube2.transform;
                U8.transform.parent = Cube2.transform;
                U9.transform.parent = Cube2.transform;
                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                u();
                keypressed = false;
            }
        }
    }
    public void uprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            U1.transform.parent = U.transform;
            U2.transform.parent = U.transform;
            U3.transform.parent = U.transform;
            U4.transform.parent = U.transform;
            U6.transform.parent = U.transform;
            U7.transform.parent = U.transform;
            U8.transform.parent = U.transform;
            U9.transform.parent = U.transform;
            U.transform.Rotate(0, - speed, 0 * Time.deltaTime);
            if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 271.5)
            {
                hasrotated = true;
                U.transform.rotation = Quaternion.Euler(0, -90, 0);
                U1.transform.parent = Cube2.transform;
                U2.transform.parent = Cube2.transform;
                U3.transform.parent = Cube2.transform;
                U4.transform.parent = Cube2.transform;
                U6.transform.parent = Cube2.transform;
                U7.transform.parent = Cube2.transform;
                U8.transform.parent = Cube2.transform;
                U9.transform.parent = Cube2.transform;
                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                uprime();
                keypressed = false;
            }
        }
    }
    public void fmove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            F1.transform.parent = F.transform;
            F2.transform.parent = F.transform;
            F3.transform.parent = F.transform;
            F4.transform.parent = F.transform;
            F6.transform.parent = F.transform;
            F7.transform.parent = F.transform;
            F8.transform.parent = F.transform;
            F9.transform.parent = F.transform;
            F.transform.Rotate(0, 0, -speed * 60 * Time.deltaTime);
            if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 271.5)
            {
                hasrotated = true;
                F.transform.rotation = Quaternion.Euler(0, 0, -90);
                F1.transform.parent = Cube2.transform;
                F2.transform.parent = Cube2.transform;
                F3.transform.parent = Cube2.transform;
                F4.transform.parent = Cube2.transform;
                F6.transform.parent = Cube2.transform;
                F7.transform.parent = Cube2.transform;
                F8.transform.parent = Cube2.transform;
                F9.transform.parent = Cube2.transform;
                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                f();
                keypressed = false;
            }
        }
    }
    public void fprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            F1.transform.parent = F.transform;
            F2.transform.parent = F.transform;
            F3.transform.parent = F.transform;
            F4.transform.parent = F.transform;
            F6.transform.parent = F.transform;
            F7.transform.parent = F.transform;
            F8.transform.parent = F.transform;
            F9.transform.parent = F.transform;
            F.transform.Rotate(0, 0, speed * 60 * Time.deltaTime);
            if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 91.5)
            {
                hasrotated = true;
                F.transform.rotation = Quaternion.Euler(0, 0, 90);
                F1.transform.parent = Cube2.transform;
                F2.transform.parent = Cube2.transform;
                F3.transform.parent = Cube2.transform;
                F4.transform.parent = Cube2.transform;
                F6.transform.parent = Cube2.transform;
                F7.transform.parent = Cube2.transform;
                F8.transform.parent = Cube2.transform;
                F9.transform.parent = Cube2.transform;
                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                fprime();
                keypressed = false;
            }
        }
    }
    public void dmove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            D1.transform.parent = D.transform;
            D2.transform.parent = D.transform;
            D3.transform.parent = D.transform;
            D4.transform.parent = D.transform;
            D6.transform.parent = D.transform;
            D7.transform.parent = D.transform;
            D8.transform.parent = D.transform;
            D9.transform.parent = D.transform;
            D.transform.Rotate(0, -speed, 0 * Time.deltaTime);
            if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 271.5)
            {
                hasrotated = true;
                D.transform.rotation = Quaternion.Euler(0, -90, 0);
                D1.transform.parent = Cube2.transform;
                D2.transform.parent = Cube2.transform;
                D3.transform.parent = Cube2.transform;
                D4.transform.parent = Cube2.transform;
                D6.transform.parent = Cube2.transform;
                D7.transform.parent = Cube2.transform;
                D8.transform.parent = Cube2.transform;
                D9.transform.parent = Cube2.transform;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
                d();
                keypressed = false;
            }
        }
    }
    public void dprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            D1.transform.parent = D.transform;
            D2.transform.parent = D.transform;
            D3.transform.parent = D.transform;
            D4.transform.parent = D.transform;
            D6.transform.parent = D.transform;
            D7.transform.parent = D.transform;
            D8.transform.parent = D.transform;
            D9.transform.parent = D.transform;
            D.transform.Rotate(0, speed, 0 * Time.deltaTime);
            if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 91.5)
            {
                hasrotated = true;
                D.transform.rotation = Quaternion.Euler(0, 90, 0);
                D1.transform.parent = Cube2.transform;
                D2.transform.parent = Cube2.transform;
                D3.transform.parent = Cube2.transform;
                D4.transform.parent = Cube2.transform;
                D6.transform.parent = Cube2.transform;
                D7.transform.parent = Cube2.transform;
                D8.transform.parent = Cube2.transform;
                D9.transform.parent = Cube2.transform;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
                dprime();
                keypressed = false;
            }
        }
    }
    public void lmove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            L1.transform.parent = L.transform;
            L2.transform.parent = L.transform;
            L3.transform.parent = L.transform;
            L4.transform.parent = L.transform;
            L6.transform.parent = L.transform;
            L7.transform.parent = L.transform;
            L8.transform.parent = L.transform;
            L9.transform.parent = L.transform;
            L.transform.Rotate(-speed, 0, 0 * Time.deltaTime);
            if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 271.5)
            {
                hasrotated = true;
                L.transform.rotation = Quaternion.Euler(-90, 0, 0);
                L1.transform.parent = Cube2.transform;
                L2.transform.parent = Cube2.transform;
                L3.transform.parent = Cube2.transform;
                L4.transform.parent = Cube2.transform;
                L6.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                L9.transform.parent = Cube2.transform;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
                l();
                keypressed = false;
            }
        }
    }
    public void lprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            L1.transform.parent = L.transform;
            L2.transform.parent = L.transform;
            L3.transform.parent = L.transform;
            L4.transform.parent = L.transform;
            L6.transform.parent = L.transform;
            L7.transform.parent = L.transform;
            L8.transform.parent = L.transform;
            L9.transform.parent = L.transform;
            L.transform.Rotate(speed, 0, 0 * Time.deltaTime);
            if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 91.5)
            {
                hasrotated = true;
                L.transform.rotation = Quaternion.Euler(90, 0, 0);
                L1.transform.parent = Cube2.transform;
                L2.transform.parent = Cube2.transform;
                L3.transform.parent = Cube2.transform;
                L4.transform.parent = Cube2.transform;
                L6.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                L9.transform.parent = Cube2.transform;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
                lprime();
                keypressed = false;
            }
        }
    }
    public void bmove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            B1.transform.parent = B.transform;
            B2.transform.parent = B.transform;
            B3.transform.parent = B.transform;
            B4.transform.parent = B.transform;
            B6.transform.parent = B.transform;
            B7.transform.parent = B.transform;
            B8.transform.parent = B.transform;
            B9.transform.parent = B.transform;
            B.transform.Rotate(0, 0, speed * 60 * Time.deltaTime);
            if (Mathf.Abs(B.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(B.transform.rotation.eulerAngles.z) < 91.5)
            {
                hasrotated = true;
                B.transform.rotation = Quaternion.Euler(0, 0, 90);
                B1.transform.parent = Cube2.transform;
                B2.transform.parent = Cube2.transform;
                B3.transform.parent = Cube2.transform;
                B4.transform.parent = Cube2.transform;
                B6.transform.parent = Cube2.transform;
                B7.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                B9.transform.parent = Cube2.transform;
                B.transform.rotation = Quaternion.Euler(0, 0, 0);
                b();
                keypressed = false;
            }
        }
    }
    public void bprimemove(ref bool keypressed, bool hasrotated)
    {
        if (!hasrotated)
        {
            B1.transform.parent = B.transform;
            B2.transform.parent = B.transform;
            B3.transform.parent = B.transform;
            B4.transform.parent = B.transform;
            B6.transform.parent = B.transform;
            B7.transform.parent = B.transform;
            B8.transform.parent = B.transform;
            B9.transform.parent = B.transform;
            B.transform.Rotate(0, 0, -speed * 60 * Time.deltaTime);
            if (Mathf.Abs(B.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(B.transform.rotation.eulerAngles.z) < 271.5)
            {
                hasrotated = true;
                B.transform.rotation = Quaternion.Euler(0, 0, -90);
                B1.transform.parent = Cube2.transform;
                B2.transform.parent = Cube2.transform;
                B3.transform.parent = Cube2.transform;
                B4.transform.parent = Cube2.transform;
                B6.transform.parent = Cube2.transform;
                B7.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                B9.transform.parent = Cube2.transform;
                B.transform.rotation = Quaternion.Euler(0, 0, 0);
                bprime();
                keypressed = false;
            }
        }
    }*/
    public void u()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 6)
            {
                ufrom[i].transform.GetChild(ufrom[i].transform.childCount - 2).parent = uto[i].transform;
            }
            else
            {
                ufrom[i].transform.GetChild(ufrom[i].transform.childCount - 1).parent = uto[i].transform;
            }          
        }
        for (int i = 0; i < 8; i++)
        {
            if (ufrom[i].transform.childCount == 4)
            {
                ufrom[i].transform.GetChild(0).GetChild(0).parent = uto[i].transform.GetChild(0);
                ufrom[i].transform.GetChild(1).GetChild(0).parent = uto[i].transform.GetChild(1);
                ufrom[i].transform.GetChild(2).GetChild(0).parent = uto[i].transform.GetChild(2);
            }
            else
            {
                ufrom[i].transform.GetChild(0).GetChild(0).parent = uto[i].transform.GetChild(0);
                ufrom[i].transform.GetChild(1).GetChild(0).parent = uto[i].transform.GetChild(1);
            }
        }
    }
    public void uprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 2)
            {
                ufrom[i].transform.GetChild(ufrom[i].transform.childCount - 2).parent = uprimeto[i].transform;
            }
            else
            {
                ufrom[i].transform.GetChild(ufrom[i].transform.childCount - 1).parent = uprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (ufrom[i].transform.childCount == 4)
            {
                ufrom[i].transform.GetChild(0).GetChild(0).parent = uprimeto[i].transform.GetChild(0);
                ufrom[i].transform.GetChild(1).GetChild(0).parent = uprimeto[i].transform.GetChild(1);
                ufrom[i].transform.GetChild(2).GetChild(0).parent = uprimeto[i].transform.GetChild(2);
            }
            else
            {
                ufrom[i].transform.GetChild(0).GetChild(0).parent = uprimeto[i].transform.GetChild(0);
                ufrom[i].transform.GetChild(1).GetChild(0).parent = uprimeto[i].transform.GetChild(1);
            }
        }
    }
    public void r()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 2 || i == 4 || i == 6 || i == 7)
            {
                rfrom[i].transform.GetChild(rfrom[i].transform.childCount - 2).parent = rto[i].transform;
            }
            else
            {
                rfrom[i].transform.GetChild(rfrom[i].transform.childCount - 1).parent = rto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (rfrom[i].transform.childCount == 4)
            {
                if (i == 0 || i == 7)
                {
                    rfrom[i].transform.GetChild(0).GetChild(0).parent = rto[i].transform.GetChild(2);
                    rfrom[i].transform.GetChild(1).GetChild(0).parent = rto[i].transform.GetChild(0);
                    rfrom[i].transform.GetChild(2).GetChild(0).parent = rto[i].transform.GetChild(1);
                }
                else
                {
                    rfrom[i].transform.GetChild(0).GetChild(0).parent = rto[i].transform.GetChild(1);
                    rfrom[i].transform.GetChild(1).GetChild(0).parent = rto[i].transform.GetChild(2);
                    rfrom[i].transform.GetChild(2).GetChild(0).parent = rto[i].transform.GetChild(0);
                }
            }
            else
            {
                rfrom[i].transform.GetChild(0).GetChild(0).parent = rto[i].transform.GetChild(1);
                rfrom[i].transform.GetChild(1).GetChild(0).parent = rto[i].transform.GetChild(0);
            }
        }
    }
    public void rprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 3 || i >= 5)
            {
                rfrom[i].transform.GetChild(rfrom[i].transform.childCount - 2).parent = rprimeto[i].transform;
            }
            else
            {
                rfrom[i].transform.GetChild(rfrom[i].transform.childCount - 1).parent = rprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (rfrom[i].transform.childCount == 4)
            {if (i == 0 || i == 7)
                {
                    rfrom[i].transform.GetChild(0).GetChild(0).parent = rprimeto[i].transform.GetChild(2);
                    rfrom[i].transform.GetChild(1).GetChild(0).parent = rprimeto[i].transform.GetChild(0);
                    rfrom[i].transform.GetChild(2).GetChild(0).parent = rprimeto[i].transform.GetChild(1);
                }
                else
                {
                    rfrom[i].transform.GetChild(0).GetChild(0).parent = rprimeto[i].transform.GetChild(1);
                    rfrom[i].transform.GetChild(1).GetChild(0).parent = rprimeto[i].transform.GetChild(2);
                    rfrom[i].transform.GetChild(2).GetChild(0).parent = rprimeto[i].transform.GetChild(0);
                }
            }
            else
            {
                rfrom[i].transform.GetChild(0).GetChild(0).parent = rprimeto[i].transform.GetChild(1);
                rfrom[i].transform.GetChild(1).GetChild(0).parent = rprimeto[i].transform.GetChild(0);
            }
        }
    }
    public void f()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 2 || i == 4 || i == 6 || i == 7)
            {
                ffrom[i].transform.GetChild(ffrom[i].transform.childCount - 2).parent = fto[i].transform;
            }
            else
            {
                ffrom[i].transform.GetChild(ffrom[i].transform.childCount - 1).parent = fto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (ffrom[i].transform.childCount == 4)
            {
                if (i == 7 || i == 5)
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fto[i].transform.GetChild(0);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fto[i].transform.GetChild(1);
                    ffrom[i].transform.GetChild(2).GetChild(0).parent = fto[i].transform.GetChild(2);
                }
                else
                {
                    if (i == 0)
                    {
                        ffrom[i].transform.GetChild(0).GetChild(0).parent = fto[i].transform.GetChild(2);
                        ffrom[i].transform.GetChild(1).GetChild(0).parent = fto[i].transform.GetChild(0);
                        ffrom[i].transform.GetChild(2).GetChild(0).parent = fto[i].transform.GetChild(1);
                    }
                    else
                    {
                        ffrom[i].transform.GetChild(0).GetChild(0).parent = fto[i].transform.GetChild(1);
                        ffrom[i].transform.GetChild(1).GetChild(0).parent = fto[i].transform.GetChild(2);
                        ffrom[i].transform.GetChild(2).GetChild(0).parent = fto[i].transform.GetChild(0);
                    }
                }
            }
            else
            {
                if (i == 1 || i == 4)
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fto[i].transform.GetChild(0);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fto[i].transform.GetChild(1);
                }
                else
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fto[i].transform.GetChild(1);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fto[i].transform.GetChild(0);
                }
            }   
        }
    }
    public void fprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 3 || i >= 5)
            {
                ffrom[i].transform.GetChild(ffrom[i].transform.childCount - 2).parent = fprimeto[i].transform;
            }
            else
            {
                ffrom[i].transform.GetChild(ffrom[i].transform.childCount - 1).parent = fprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (ffrom[i].transform.childCount == 4)
            {
                if (i == 7)
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fprimeto[i].transform.GetChild(2);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fprimeto[i].transform.GetChild(0);
                    ffrom[i].transform.GetChild(2).GetChild(0).parent = fprimeto[i].transform.GetChild(1);
                }
                else
                {
                    if (i == 0 || i == 5)
                    {
                        ffrom[i].transform.GetChild(0).GetChild(0).parent = fprimeto[i].transform.GetChild(0);
                        ffrom[i].transform.GetChild(1).GetChild(0).parent = fprimeto[i].transform.GetChild(1);
                        ffrom[i].transform.GetChild(2).GetChild(0).parent = fprimeto[i].transform.GetChild(2);
                    }
                    else
                    {
                        ffrom[i].transform.GetChild(0).GetChild(0).parent = fprimeto[i].transform.GetChild(1);
                        ffrom[i].transform.GetChild(1).GetChild(0).parent = fprimeto[i].transform.GetChild(2);
                        ffrom[i].transform.GetChild(2).GetChild(0).parent = fprimeto[i].transform.GetChild(0);
                    }
                }
            }
            else
            {
                if (i == 6 || i == 4)
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fprimeto[i].transform.GetChild(0);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fprimeto[i].transform.GetChild(1);
                }
                else
                {
                    ffrom[i].transform.GetChild(0).GetChild(0).parent = fprimeto[i].transform.GetChild(1);
                    ffrom[i].transform.GetChild(1).GetChild(0).parent = fprimeto[i].transform.GetChild(0);
                }
            }
        }
    }
    public void d()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 2 || i == 4 || i == 6 || i == 7)
            {
                dfrom[i].transform.GetChild(dfrom[i].transform.childCount - 2).parent = dto[i].transform;
            }
            else
            {
                dfrom[i].transform.GetChild(dfrom[i].transform.childCount - 1).parent = dto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (dfrom[i].transform.childCount == 4)
            {
                if (i == 0)
                {
                    dfrom[i].transform.GetChild(0).GetChild(0).parent = dto[i].transform.GetChild(2);
                    dfrom[i].transform.GetChild(1).GetChild(0).parent = dto[i].transform.GetChild(0);
                    dfrom[i].transform.GetChild(2).GetChild(0).parent = dto[i].transform.GetChild(1);
                }
                else
                {
                    if (i == 7)
                    {
                        dfrom[i].transform.GetChild(0).GetChild(0).parent = dto[i].transform.GetChild(1);
                        dfrom[i].transform.GetChild(1).GetChild(0).parent = dto[i].transform.GetChild(2);
                        dfrom[i].transform.GetChild(2).GetChild(0).parent = dto[i].transform.GetChild(0);
                    }
                    else
                    {
                        dfrom[i].transform.GetChild(0).GetChild(0).parent = dto[i].transform.GetChild(0);
                        dfrom[i].transform.GetChild(1).GetChild(0).parent = dto[i].transform.GetChild(1);
                        dfrom[i].transform.GetChild(2).GetChild(0).parent = dto[i].transform.GetChild(2);
                    }
                }             
            }
            else
            {
                dfrom[i].transform.GetChild(0).GetChild(0).parent = dto[i].transform.GetChild(0);
                dfrom[i].transform.GetChild(1).GetChild(0).parent = dto[i].transform.GetChild(1);
            }
        }
    }
    public void dprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 3 || i == 5 || i == 6 || i == 7)
            {
                dfrom[i].transform.GetChild(dfrom[i].transform.childCount - 2).parent = dprimeto[i].transform;
            }
            else
            {
                dfrom[i].transform.GetChild(dfrom[i].transform.childCount - 1).parent = dprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (dfrom[i].transform.childCount == 4)
            {
                if (i == 5)
                {
                    dfrom[i].transform.GetChild(0).GetChild(0).parent = dprimeto[i].transform.GetChild(2);
                    dfrom[i].transform.GetChild(1).GetChild(0).parent = dprimeto[i].transform.GetChild(0);
                    dfrom[i].transform.GetChild(2).GetChild(0).parent = dprimeto[i].transform.GetChild(1);
                }
                else
                {
                    if (i == 2)
                    {
                        dfrom[i].transform.GetChild(0).GetChild(0).parent = dprimeto[i].transform.GetChild(1);
                        dfrom[i].transform.GetChild(1).GetChild(0).parent = dprimeto[i].transform.GetChild(2);
                        dfrom[i].transform.GetChild(2).GetChild(0).parent = dprimeto[i].transform.GetChild(0);
                    }
                    else
                    {
                        dfrom[i].transform.GetChild(0).GetChild(0).parent = dprimeto[i].transform.GetChild(0);
                        dfrom[i].transform.GetChild(1).GetChild(0).parent = dprimeto[i].transform.GetChild(1);
                        dfrom[i].transform.GetChild(2).GetChild(0).parent = dprimeto[i].transform.GetChild(2);
                    }
                }
            }
            else
            {
                dfrom[i].transform.GetChild(0).GetChild(0).parent = dprimeto[i].transform.GetChild(0);
                dfrom[i].transform.GetChild(1).GetChild(0).parent = dprimeto[i].transform.GetChild(1);
            }
        }
    }
    public void l()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 3 || i == 5 || i == 6 || i == 7)
            {
                lfrom[i].transform.GetChild(lfrom[i].transform.childCount - 2).parent = lto[i].transform;
            }
            else
            {
                lfrom[i].transform.GetChild(lfrom[i].transform.childCount - 1).parent = lto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (lfrom[i].transform.childCount == 4)
            {
                if (i == 0 || i == 2 || i == 5)
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lto[i].transform.GetChild(2);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lto[i].transform.GetChild(0);
                    lfrom[i].transform.GetChild(2).GetChild(0).parent = lto[i].transform.GetChild(1);
                }
                else
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lto[i].transform.GetChild(0);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lto[i].transform.GetChild(1);
                    lfrom[i].transform.GetChild(2).GetChild(0).parent = lto[i].transform.GetChild(2);
                }
            }
            else
            {
                if (i == 4 || i == 6)
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lto[i].transform.GetChild(1);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lto[i].transform.GetChild(0);
                }
                else
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lto[i].transform.GetChild(0);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lto[i].transform.GetChild(1);
                }
            }
        }
    }
    public void lprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 2 || i == 4 || i == 6 || i == 7)
            {
                lfrom[i].transform.GetChild(lfrom[i].transform.childCount - 2).parent = lprimeto[i].transform;
            }
            else
            {
                lfrom[i].transform.GetChild(lfrom[i].transform.childCount - 1).parent = lprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (lfrom[i].transform.childCount == 4)
            {
                if (i == 7 || i == 5 || i == 0)
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lprimeto[i].transform.GetChild(1);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lprimeto[i].transform.GetChild(2);
                    lfrom[i].transform.GetChild(2).GetChild(0).parent = lprimeto[i].transform.GetChild(0);
                }
                else
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lprimeto[i].transform.GetChild(0);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lprimeto[i].transform.GetChild(1);
                    lfrom[i].transform.GetChild(2).GetChild(0).parent = lprimeto[i].transform.GetChild(2);
                }
            }
            else
            {
                if (i == 4 || i == 2)
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lprimeto[i].transform.GetChild(1);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lprimeto[i].transform.GetChild(0);
                }
                else
                {
                    lfrom[i].transform.GetChild(0).GetChild(0).parent = lprimeto[i].transform.GetChild(0);
                    lfrom[i].transform.GetChild(1).GetChild(0).parent = lprimeto[i].transform.GetChild(1);
                }
            }
        }/*
        L3.transform.GetChild(0).parent = L1.transform;
        L2.transform.GetChild(0).parent = L4.transform;
        L1.transform.GetChild(0).parent = L7.transform;
        L6.transform.GetChild(0).parent = L2.transform;
        L4.transform.GetChild(0).parent = L8.transform;
        L9.transform.GetChild(0).parent = L3.transform;
        L8.transform.GetChild(0).parent = L6.transform;
        L7.transform.GetChild(0).parent = L9.transform;*/
    }
    public void b()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 3 || i == 5 || i == 6 || i == 7)
            {
                bfrom[i].transform.GetChild(bfrom[i].transform.childCount - 2).parent = bto[i].transform;
            }
            else
            {
                bfrom[i].transform.GetChild(bfrom[i].transform.childCount - 1).parent = bto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (bfrom[i].transform.childCount == 4)
            {
                if (i == 0 || i == 2)
                {
                    bfrom[i].transform.GetChild(0).GetChild(0).parent = bto[i].transform.GetChild(2);
                    bfrom[i].transform.GetChild(1).GetChild(0).parent = bto[i].transform.GetChild(0);
                    bfrom[i].transform.GetChild(2).GetChild(0).parent = bto[i].transform.GetChild(1);
                }
                else
                {
                    bfrom[i].transform.GetChild(0).GetChild(0).parent = bto[i].transform.GetChild(1);
                    bfrom[i].transform.GetChild(1).GetChild(0).parent = bto[i].transform.GetChild(2);
                    bfrom[i].transform.GetChild(2).GetChild(0).parent = bto[i].transform.GetChild(0);
                }
            }
            else
            {
                bfrom[i].transform.GetChild(0).GetChild(0).parent = bto[i].transform.GetChild(0);
                bfrom[i].transform.GetChild(1).GetChild(0).parent = bto[i].transform.GetChild(1);
            }
        }
    }
    public void bprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i == 2 || i == 4 || i == 6 || i == 7)
            {
                bfrom[i].transform.GetChild(bfrom[i].transform.childCount - 2).parent = bprimeto[i].transform;
            }
            else
            {
                bfrom[i].transform.GetChild(bfrom[i].transform.childCount - 1).parent = bprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (bfrom[i].transform.childCount == 4)
            {
                if (i == 2 || i == 7)
                {
                    bfrom[i].transform.GetChild(0).GetChild(0).parent = bprimeto[i].transform.GetChild(2);
                    bfrom[i].transform.GetChild(1).GetChild(0).parent = bprimeto[i].transform.GetChild(0);
                    bfrom[i].transform.GetChild(2).GetChild(0).parent = bprimeto[i].transform.GetChild(1);
                }
                else
                {
                    bfrom[i].transform.GetChild(0).GetChild(0).parent = bprimeto[i].transform.GetChild(1);
                    bfrom[i].transform.GetChild(1).GetChild(0).parent = bprimeto[i].transform.GetChild(2);
                    bfrom[i].transform.GetChild(2).GetChild(0).parent = bprimeto[i].transform.GetChild(0);
                }
            }
            else
            {
                bfrom[i].transform.GetChild(0).GetChild(0).parent = bprimeto[i].transform.GetChild(0);
                bfrom[i].transform.GetChild(1).GetChild(0).parent = bprimeto[i].transform.GetChild(1);
            }
        }
    }
    public void m()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 6)
            {
                mfrom[i].transform.GetChild(mfrom[i].transform.childCount - 2).parent = mto[i].transform;
            }
            else
            {
                mfrom[i].transform.GetChild(mfrom[i].transform.childCount - 1).parent = mto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (mfrom[i].transform.childCount == 3)
            {
                mfrom[i].transform.GetChild(0).GetChild(0).parent = mto[i].transform.GetChild(1);
                mfrom[i].transform.GetChild(1).GetChild(0).parent = mto[i].transform.GetChild(0);
            }
        }
    }
    public void mprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 2)
            {
                mfrom[i].transform.GetChild(mfrom[i].transform.childCount - 2).parent = mprimeto[i].transform;
            }
            else
            {
                mfrom[i].transform.GetChild(mfrom[i].transform.childCount - 1).parent = mprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (mfrom[i].transform.childCount == 3)
            {
                mfrom[i].transform.GetChild(0).GetChild(0).parent = mprimeto[i].transform.GetChild(1);
                mfrom[i].transform.GetChild(1).GetChild(0).parent = mprimeto[i].transform.GetChild(0);
            }
        }
    }
    public void e()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 2)
            {
                efrom[i].transform.GetChild(efrom[i].transform.childCount - 2).parent = eto[i].transform;
            }
            else
            {
                efrom[i].transform.GetChild(efrom[i].transform.childCount - 1).parent = eto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (efrom[i].transform.childCount == 3)
            {   if (i == 2 || i == 4)
                {
                    efrom[i].transform.GetChild(0).GetChild(0).parent = eto[i].transform.GetChild(1);
                    efrom[i].transform.GetChild(1).GetChild(0).parent = eto[i].transform.GetChild(0);
                }
                else
                {
                    efrom[i].transform.GetChild(0).GetChild(0).parent = eto[i].transform.GetChild(0);
                    efrom[i].transform.GetChild(1).GetChild(0).parent = eto[i].transform.GetChild(1);
                }
            }
        }
    }
    public void eprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 6)
            {
                efrom[i].transform.GetChild(efrom[i].transform.childCount - 2).parent = eprimeto[i].transform;
            }
            else
            {
                efrom[i].transform.GetChild(efrom[i].transform.childCount - 1).parent = eprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (efrom[i].transform.childCount == 3)
            {
                if (i == 6 || i == 4)
                {
                    efrom[i].transform.GetChild(0).GetChild(0).parent = eprimeto[i].transform.GetChild(1);
                    efrom[i].transform.GetChild(1).GetChild(0).parent = eprimeto[i].transform.GetChild(0);
                }
                else
                {
                    efrom[i].transform.GetChild(0).GetChild(0).parent = eprimeto[i].transform.GetChild(0);
                    efrom[i].transform.GetChild(1).GetChild(0).parent = eprimeto[i].transform.GetChild(1);
                }
            }
        }
    }
    public void s()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 2)
            {
                sfrom[i].transform.GetChild(sfrom[i].transform.childCount - 2).parent = sto[i].transform;
            }
            else
            {
                sfrom[i].transform.GetChild(sfrom[i].transform.childCount - 1).parent = sto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (sfrom[i].transform.childCount == 3)
            {
                sfrom[i].transform.GetChild(0).GetChild(0).parent = sto[i].transform.GetChild(1);
                sfrom[i].transform.GetChild(1).GetChild(0).parent = sto[i].transform.GetChild(0);
            }
        }
    }
    public void sprime()
    {
        for (int i = 0; i < 8; i++)
        {
            if (i >= 6)
            {
                sfrom[i].transform.GetChild(sfrom[i].transform.childCount - 2).parent = sprimeto[i].transform;
            }
            else
            {
                sfrom[i].transform.GetChild(sfrom[i].transform.childCount - 1).parent = sprimeto[i].transform;
            }
        }
        for (int i = 0; i < 8; i++)
        {
            if (sfrom[i].transform.childCount == 3)
            {
                sfrom[i].transform.GetChild(0).GetChild(0).parent = sprimeto[i].transform.GetChild(1);
                sfrom[i].transform.GetChild(1).GetChild(0).parent = sprimeto[i].transform.GetChild(0);
            }
        }
    }
    /*public void scramble()
    {
        scramblestr = "B2 U2 F' D2 B' D2 B2 F' D2 F U' F U' L U' F2 U2 L F'";
        scramblelist = scramblestr.Split(' ');
        Debug.Log(scramblelist);
    }*/
    
}
