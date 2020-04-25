using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class F2script : MonoBehaviour
{
    public GameObject u8sticker;
    public GameObject f2sticker;
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
    public GameObject F1;
    public GameObject F2;
    public GameObject F3;
    public GameObject F4;
    public GameObject F;
    public GameObject F6;
    public GameObject F7;
    public GameObject F8;
    public GameObject F9;
    public GameObject D;
    public GameObject B8;
    public GameObject B2;
    public GameObject B;
    public GameObject M;
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
    GameObject fchild;
    GameObject uchild;
    GameObject bchild;
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
            if (F2.transform.childCount > 0)
            {
                Collider collu8 = u8sticker.GetComponentInChildren<Collider>();
                Collider collf2 = f2sticker.GetComponentInChildren<Collider>();
                if (collu8.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 1;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
                if (collf2.Raycast(ray, out hit, 100.0f))
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
                        // M
                        F2.transform.parent = M.transform;
                        F.transform.parent = M.transform;
                        F8.transform.parent = M.transform;
                        D.transform.parent = M.transform;
                        B8.transform.parent = M.transform;
                        B.transform.parent = M.transform;
                        B2.transform.parent = M.transform;
                        U.transform.parent = M.transform;
                        M.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
                        mousedir = 2;
                    }
                    if (deltapos.y < 0 && deltapos.x > 0)
                    {
                        // F
                        F1.transform.parent = F.transform;
                        F2.transform.parent = F.transform;
                        F3.transform.parent = F.transform;
                        F4.transform.parent = F.transform;
                        F6.transform.parent = F.transform;
                        F7.transform.parent = F.transform;
                        F8.transform.parent = F.transform;
                        F9.transform.parent = F.transform;
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (deltapos.y > 0 && deltapos.x < 0)
                    {
                        // F
                        F1.transform.parent = F.transform;
                        F2.transform.parent = F.transform;
                        F3.transform.parent = F.transform;
                        F4.transform.parent = F.transform;
                        F6.transform.parent = F.transform;
                        F7.transform.parent = F.transform;
                        F8.transform.parent = F.transform;
                        F9.transform.parent = F.transform;
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (deltapos.y < 0 && deltapos.x < 0)
                    {
                        // M
                        F2.transform.parent = M.transform;
                        F.transform.parent = M.transform;
                        F8.transform.parent = M.transform;
                        D.transform.parent = M.transform;
                        B8.transform.parent = M.transform;
                        B.transform.parent = M.transform;
                        B2.transform.parent = M.transform;
                        U.transform.parent = M.transform;
                        M.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
                        mousedir = 2;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 271.5)
                    {
                        hasrotated = true;
                        F.transform.rotation = Quaternion.Euler(0, 0, -90);
                    }
                    if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 91.5)
                    {
                        hasrotated = true;
                        F.transform.rotation = Quaternion.Euler(0, 0, 90);
                    }
                    else
                    {
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
                    }
                }
                if (mousedir == 2)
                {
                    if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 271.5)
                    {
                        hasrotated = true;
                        M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                    }
                    if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 91.5)
                    {
                        hasrotated = true;
                        M.transform.rotation = Quaternion.Euler(90, 0, 0);
                    }
                    else
                    {
                        M.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                    }
                }
            }
            if (Input.GetMouseButtonUp(0))
            {
                finalpos = Input.mousePosition;
                deltapos = finalpos - inicialpos;
                if (mousedir == 1)
                {
                    if (F.transform.rotation.eulerAngles.z > 330)
                    {
                        F.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (F.transform.rotation.eulerAngles.z > 265)
                        {
                            F.transform.rotation = Quaternion.Euler(0, 0, -90);
                            layerRotation.f();
                        }
                        else
                        {
                            if (F.transform.rotation.eulerAngles.z > 30)
                            {
                                F.transform.rotation = Quaternion.Euler(0, 0, 90);
                                layerRotation.fprime();
                            }
                            else
                            {
                                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    F1.transform.parent = Cube2.transform;
                    F2.transform.parent = Cube2.transform;
                    F3.transform.parent = Cube2.transform;
                    F4.transform.parent = Cube2.transform;
                    F6.transform.parent = Cube2.transform;
                    F7.transform.parent = Cube2.transform;
                    F8.transform.parent = Cube2.transform;
                    F9.transform.parent = Cube2.transform;
                    F.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                if (mousedir == 2)
                {
                    if (M.transform.rotation.eulerAngles.x > 330)
                    {
                        M.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (M.transform.rotation.eulerAngles.x > 265)
                        {
                            M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                            layerRotation.m();
                        }
                        else
                        {
                            if (M.transform.rotation.eulerAngles.x > 30)
                            {
                                M.transform.rotation = Quaternion.Euler(90, 0, 0);
                                layerRotation.mprime();
                            }
                            else
                            {
                                M.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    F2.transform.parent = Cube2.transform;
                    F.transform.parent = Cube2.transform;
                    F8.transform.parent = Cube2.transform;
                    D.transform.parent = Cube2.transform;
                    B8.transform.parent = Cube2.transform;
                    B.transform.parent = Cube2.transform;
                    B2.transform.parent = Cube2.transform;
                    U.transform.parent = Cube2.transform;
                    M.transform.rotation = Quaternion.Euler(0, 0, 0);
                    uchild = U.transform.GetChild(0).gameObject;
                    uchild.transform.parent = null;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    U.transform.position = new Vector3(0, 4, 0);
                    uchild.transform.parent = U.transform;
                    fchild = F.transform.GetChild(0).gameObject;
                    fchild.transform.parent = null;
                    F.transform.rotation = Quaternion.Euler(0, 0, 0);
                    F.transform.position = new Vector3(0, 2, -2);
                    fchild.transform.parent = F.transform;
                    dchild = D.transform.GetChild(0).gameObject;
                    dchild.transform.parent = null;
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                    D.transform.position = new Vector3(0, 0, 0);
                    dchild.transform.parent = D.transform;
                    bchild = B.transform.GetChild(0).gameObject;
                    bchild.transform.parent = null;
                    B.transform.rotation = Quaternion.Euler(0, 0, 0);
                    B.transform.position = new Vector3(0, 2, 2);
                    bchild.transform.parent = B.transform;
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
                        // M
                        F2.transform.parent = M.transform;
                        F.transform.parent = M.transform;
                        F8.transform.parent = M.transform;
                        D.transform.parent = M.transform;
                        B8.transform.parent = M.transform;
                        B.transform.parent = M.transform;
                        B2.transform.parent = M.transform;
                        U.transform.parent = M.transform;
                        M.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
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
                    if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 271.5)
                    {
                        hasrotated = true;
                        M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                    }
                    if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 91.5)
                    {
                        hasrotated = true;
                        M.transform.rotation = Quaternion.Euler(90, 0, 0);
                    }
                    else
                    {
                        M.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
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
                    if (M.transform.rotation.eulerAngles.x > 330)
                    {
                        M.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (M.transform.rotation.eulerAngles.x > 265)
                        {
                            M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                            layerRotation.m();
                        }
                        else
                        {
                            if (M.transform.rotation.eulerAngles.x > 30)
                            {
                                M.transform.rotation = Quaternion.Euler(90, 0, 0);
                                layerRotation.mprime();
                            }
                            else
                            {
                                M.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    F2.transform.parent = Cube2.transform;
                    F.transform.parent = Cube2.transform;
                    F8.transform.parent = Cube2.transform;
                    D.transform.parent = Cube2.transform;
                    B8.transform.parent = Cube2.transform;
                    B.transform.parent = Cube2.transform;
                    B2.transform.parent = Cube2.transform;
                    U.transform.parent = Cube2.transform;
                    M.transform.rotation = Quaternion.Euler(0, 0, 0);
                    uchild = U.transform.GetChild(0).gameObject;
                    uchild.transform.parent = null;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    U.transform.position = new Vector3(0, 4, 0);
                    uchild.transform.parent = U.transform;
                    fchild = F.transform.GetChild(0).gameObject;
                    fchild.transform.parent = null;
                    F.transform.rotation = Quaternion.Euler(0, 0, 0);
                    F.transform.position = new Vector3(0, 2, -2);
                    fchild.transform.parent = F.transform;
                    dchild = D.transform.GetChild(0).gameObject;
                    dchild.transform.parent = null;
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                    D.transform.position = new Vector3(0, 0, 0);
                    dchild.transform.parent = D.transform;
                    bchild = B.transform.GetChild(0).gameObject;
                    bchild.transform.parent = null;
                    B.transform.rotation = Quaternion.Euler(0, 0, 0);
                    B.transform.position = new Vector3(0, 2, 2);
                    bchild.transform.parent = B.transform;
                }
                hasrotated = false;
                mousedir = 0;
                pressed = false;
            }

        }
    }
}
