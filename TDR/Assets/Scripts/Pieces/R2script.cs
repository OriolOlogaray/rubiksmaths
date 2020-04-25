using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class R2script : MonoBehaviour
{
    public GameObject u6sticker;
    public GameObject r2sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject U1;
    public GameObject U2;
    public GameObject U3;
    public GameObject U4;
    public GameObject U;
    public GameObject U6;
    public GameObject U7;
    public GameObject U8;
    public GameObject U9;
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject D;
    public GameObject L2;
    public GameObject L;
    public GameObject L8;
    public GameObject S;
    public int correction = 55;
    private int sticker = 0;
    private int mousedir = 0;
    public int speed;
    private bool pressed = false;
    private bool hasrotated = false;
    Vector3 inicialpos = new Vector3();
    Vector3 finalpos = new Vector3();
    Vector3 deltapos = new Vector3();
    private LayerRotation layerRotation;
    GameObject rchild;
    GameObject uchild;
    GameObject lchild;
    GameObject dchild;

    void Awake()
    {
        layerRotation = Cube.GetComponent<LayerRotation>();
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (R2.transform.childCount > 0)
            {
                Collider collu6 = u6sticker.GetComponentInChildren<Collider>();
                Collider collr2 = r2sticker.GetComponentInChildren<Collider>();
                if (collu6.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 1;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
                if (collr2.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 2;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
            }
        }
        if (sticker == 1)
        {
            if (pressed == true && !hasrotated)
            {
                if (mousedir == 0)
                {
                    deltapos = Input.mousePosition - inicialpos;
                    if (deltapos.y > 0 && deltapos.x > 0)
                    {
                        //R
                        R1.transform.parent = R.transform;
                        R2.transform.parent = R.transform;
                        R3.transform.parent = R.transform;
                        R4.transform.parent = R.transform;
                        R6.transform.parent = R.transform;
                        R7.transform.parent = R.transform;
                        R8.transform.parent = R.transform;
                        R9.transform.parent = R.transform;
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (deltapos.y < 0 && deltapos.x > 0)
                    {
                        // S
                        L2.transform.parent = S.transform;
                        U.transform.parent = S.transform;
                        R2.transform.parent = S.transform;
                        R.transform.parent = S.transform;
                        R8.transform.parent = S.transform;
                        D.transform.parent = S.transform;
                        L8.transform.parent = S.transform;
                        L.transform.parent = S.transform;
                        S.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) * correction / 4 * Time.deltaTime);
                        mousedir = 2;
                    }
                    if (deltapos.y > 0 && deltapos.x < 0)
                    {
                        // S
                        L2.transform.parent = S.transform;
                        U.transform.parent = S.transform;
                        R2.transform.parent = S.transform;
                        R.transform.parent = S.transform;
                        R8.transform.parent = S.transform;
                        D.transform.parent = S.transform;
                        L8.transform.parent = S.transform;
                        L.transform.parent = S.transform;
                        S.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X") * correction) / 4 * Time.deltaTime);
                        mousedir = 2;
                    }
                    if (deltapos.y < 0 && deltapos.x < 0)
                    {
                        //R
                        R1.transform.parent = R.transform;
                        R2.transform.parent = R.transform;
                        R3.transform.parent = R.transform;
                        R4.transform.parent = R.transform;
                        R6.transform.parent = R.transform;
                        R7.transform.parent = R.transform;
                        R8.transform.parent = R.transform;
                        R9.transform.parent = R.transform;
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
                        mousedir = 1;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 271.5)
                    {
                        hasrotated = true;
                        R.transform.rotation = Quaternion.Euler(-90, 0, 0);
                    }
                    if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 91.5)
                    {
                        hasrotated = true;
                        R.transform.rotation = Quaternion.Euler(90, 0, 0);
                    }
                    else
                    {
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
                    }
                }
                if (mousedir == 2)
                {
                    if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 271.5)
                    {
                        hasrotated = true;
                        S.transform.rotation = Quaternion.Euler(0, 0, -90);
                    }
                    if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 91.5)
                    {
                        hasrotated = true;
                        S.transform.rotation = Quaternion.Euler(0, 0, 90);
                    }
                    else
                    {
                        S.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                    }
                }
            }
            if (Input.GetMouseButtonUp(0))
            {
                finalpos = Input.mousePosition;
                deltapos = finalpos - inicialpos;
                if (mousedir == 1)
                {
                    if (R.transform.rotation.eulerAngles.x > 330)
                    {
                        R.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (R.transform.rotation.eulerAngles.x > 265)
                        {
                            R.transform.rotation = Quaternion.Euler(-90, 0, 0);
                            layerRotation.rprime();
                        }
                        else
                        {
                            if (R.transform.rotation.eulerAngles.x > 30)
                            {
                                R.transform.rotation = Quaternion.Euler(90, 0, 0);
                                layerRotation.r();
                            }
                            else
                            {
                                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    R1.transform.parent = Cube2.transform;
                    R2.transform.parent = Cube2.transform;
                    R3.transform.parent = Cube2.transform;
                    R4.transform.parent = Cube2.transform;
                    R6.transform.parent = Cube2.transform;
                    R7.transform.parent = Cube2.transform;
                    R8.transform.parent = Cube2.transform;
                    R9.transform.parent = Cube2.transform;
                    R.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                if (mousedir == 2)
                {
                    if (S.transform.rotation.eulerAngles.z > 330)
                    {
                        S.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (S.transform.rotation.eulerAngles.z > 265)
                        {
                            S.transform.rotation = Quaternion.Euler(0, 0, -90);
                            layerRotation.s();
                        }
                        else
                        {
                            if (S.transform.rotation.eulerAngles.z > 30)
                            {
                                S.transform.rotation = Quaternion.Euler(0, 0, 90);
                                layerRotation.sprime();
                            }
                            else
                            {
                                S.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    L2.transform.parent = Cube2.transform;
                    U.transform.parent = Cube2.transform;
                    R2.transform.parent = Cube2.transform;
                    R.transform.parent = Cube2.transform;
                    R8.transform.parent = Cube2.transform;
                    D.transform.parent = Cube2.transform;
                    L8.transform.parent = Cube2.transform;
                    L.transform.parent = Cube2.transform;
                    S.transform.rotation = Quaternion.Euler(0, 0, 0);
                    uchild = U.transform.GetChild(0).gameObject;
                    uchild.transform.parent = null;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    U.transform.position = new Vector3(0, 4, 0);
                    uchild.transform.parent = U.transform;
                    lchild = L.transform.GetChild(0).gameObject;
                    lchild.transform.parent = null;
                    L.transform.rotation = Quaternion.Euler(0, 0, 0);
                    L.transform.position = new Vector3(-2, 2, 0);
                    lchild.transform.parent = L.transform;
                    dchild = D.transform.GetChild(0).gameObject;
                    dchild.transform.parent = null;
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                    D.transform.position = new Vector3(0, 0, 0);
                    dchild.transform.parent = D.transform;
                    rchild = R.transform.GetChild(0).gameObject;
                    rchild.transform.parent = null;
                    R.transform.rotation = Quaternion.Euler(0, 0, 0);
                    R.transform.position = new Vector3(2, 2, 0);
                    rchild.transform.parent = R.transform;
                }
                hasrotated = false;
                mousedir = 0;
                pressed = false;
            }

        }
        if (sticker == 2)
        {
            if (pressed == true && !hasrotated)
            {
                if (mousedir == 0)
                {
                    deltapos = Input.mousePosition - inicialpos;
                    if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                    {
                        // U
                        U1.transform.parent = U.transform;
                        U2.transform.parent = U.transform;
                        U3.transform.parent = U.transform;
                        U4.transform.parent = U.transform;
                        U6.transform.parent = U.transform;
                        U7.transform.parent = U.transform;
                        U8.transform.parent = U.transform;
                        U9.transform.parent = U.transform;
                        U.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (Mathf.Abs(deltapos.x) < Mathf.Abs(deltapos.y))
                    {
                        // S
                        L2.transform.parent = S.transform;
                        U.transform.parent = S.transform;
                        R2.transform.parent = S.transform;
                        R.transform.parent = S.transform;
                        R8.transform.parent = S.transform;
                        D.transform.parent = S.transform;
                        L8.transform.parent = S.transform;
                        L.transform.parent = S.transform;
                        S.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                        mousedir = 2;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 275.5)
                    {
                        hasrotated = true;
                        U.transform.rotation = Quaternion.Euler(0, -90, 0);
                    }
                    if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 95.5)
                    {
                        hasrotated = true;
                        U.transform.rotation = Quaternion.Euler(0, 90, 0);
                    }
                    else
                    {
                        U.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                    }
                }
                if (mousedir == 2)
                {
                    if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 271.5)
                    {
                        hasrotated = true;
                        S.transform.rotation = Quaternion.Euler(0, 0, -90);
                    }
                    if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 91.5)
                    {
                        hasrotated = true;
                        S.transform.rotation = Quaternion.Euler(0, 0, 90);
                    }
                    else
                    {
                        S.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                    }
                }
            }
            if (Input.GetMouseButtonUp(0))
            {
                finalpos = Input.mousePosition;
                deltapos = finalpos - inicialpos;
                if (mousedir == 1)
                {
                    if (U.transform.rotation.eulerAngles.y > 330)
                    {
                        U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (U.transform.rotation.eulerAngles.y > 265)
                        {
                            U.transform.rotation = Quaternion.Euler(0, -90, 0);
                            layerRotation.uprime();
                        }
                        else
                        {
                            if (U.transform.rotation.eulerAngles.y > 30)
                            {
                                U.transform.rotation = Quaternion.Euler(0, 90, 0);
                                layerRotation.u();
                            }
                            else
                            {
                                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    U1.transform.parent = Cube2.transform;
                    U2.transform.parent = Cube2.transform;
                    U3.transform.parent = Cube2.transform;
                    U4.transform.parent = Cube2.transform;
                    U6.transform.parent = Cube2.transform;
                    U7.transform.parent = Cube2.transform;
                    U8.transform.parent = Cube2.transform;
                    U9.transform.parent = Cube2.transform;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                if (mousedir == 2)
                {
                    if (S.transform.rotation.eulerAngles.z > 330)
                    {
                        S.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (S.transform.rotation.eulerAngles.z > 265)
                        {
                            S.transform.rotation = Quaternion.Euler(0, 0, -90);
                            layerRotation.s();
                        }
                        else
                        {
                            if (S.transform.rotation.eulerAngles.z > 30)
                            {
                                S.transform.rotation = Quaternion.Euler(0, 0, 90);
                                layerRotation.sprime();
                            }
                            else
                            {
                                S.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    L2.transform.parent = Cube2.transform;
                    U.transform.parent = Cube2.transform;
                    R2.transform.parent = Cube2.transform;
                    R.transform.parent = Cube2.transform;
                    R8.transform.parent = Cube2.transform;
                    D.transform.parent = Cube2.transform;
                    L8.transform.parent = Cube2.transform;
                    L.transform.parent = Cube2.transform;
                    S.transform.rotation = Quaternion.Euler(0, 0, 0);
                    uchild = U.transform.GetChild(0).gameObject;
                    uchild.transform.parent = null;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    U.transform.position = new Vector3(0, 4, 0);
                    uchild.transform.parent = U.transform;
                    lchild = L.transform.GetChild(0).gameObject;
                    lchild.transform.parent = null;
                    L.transform.rotation = Quaternion.Euler(0, 0, 0);
                    L.transform.position = new Vector3(-2, 2, 0);
                    lchild.transform.parent = L.transform;
                    dchild = D.transform.GetChild(0).gameObject;
                    dchild.transform.parent = null;
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                    D.transform.position = new Vector3(0, 0, 0);
                    dchild.transform.parent = D.transform;
                    rchild = R.transform.GetChild(0).gameObject;
                    rchild.transform.parent = null;
                    R.transform.rotation = Quaternion.Euler(0, 0, 0);
                    R.transform.position = new Vector3(2, 2, 0);
                    rchild.transform.parent = R.transform;
                }
                hasrotated = false;
                mousedir = 0;
                pressed = false;
            }

        }
    }
}

