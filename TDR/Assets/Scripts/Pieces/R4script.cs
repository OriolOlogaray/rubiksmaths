using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class R4script : MonoBehaviour
{
    public GameObject r4sticker;
    public GameObject f6sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject F1;
    public GameObject F2;
    public GameObject F3;
    public GameObject F4;
    public GameObject F;
    public GameObject F6;
    public GameObject F7;
    public GameObject F8;
    public GameObject F9;
    public GameObject L;
    public GameObject B;
    public GameObject L4;
    public GameObject E;
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
    GameObject lchild;
    GameObject bchild;
    GameObject rchild;

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
            if (R4.transform.childCount > 0)
            {
                Collider collr4 = r4sticker.GetComponentInChildren<Collider>();
                Collider collf6 = f6sticker.GetComponentInChildren<Collider>();
                if (collr4.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 1;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
                if (collf6.Raycast(ray, out hit, 100.0f))
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
                        if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                        {
                            // E
                            R6.transform.parent = E.transform;
                            R.transform.parent = E.transform;
                            R4.transform.parent = E.transform;
                            F.transform.parent = E.transform;
                            F4.transform.parent = E.transform;
                            L.transform.parent = E.transform;
                            L4.transform.parent = E.transform;
                            B.transform.parent = E.transform;
                            E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                            mousedir = 1;
                        }
                        if (Mathf.Abs(deltapos.x) < Mathf.Abs(deltapos.y))
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
                            F.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                            mousedir = 2;
                        }
                    }
                    if (mousedir == 1)
                    {
                        if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 275.5)
                        {
                            hasrotated = true;
                            E.transform.rotation = Quaternion.Euler(0, -90, 0);
                        }
                        if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 95.5)
                        {
                            hasrotated = true;
                            E.transform.rotation = Quaternion.Euler(0, 90, 0);
                        }
                        else
                        {
                            E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                        }
                    }
                    if (mousedir == 2)
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
                            F.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                        }
                    }
                }
                if (Input.GetMouseButtonUp(0))
                {
                    finalpos = Input.mousePosition;
                    deltapos = finalpos - inicialpos;
                    if (mousedir == 1)
                    {
                        if (E.transform.rotation.eulerAngles.y > 330)
                        {
                            E.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                        else
                        {
                            if (E.transform.rotation.eulerAngles.y > 265)
                            {
                                E.transform.rotation = Quaternion.Euler(0, -90, 0);
                                layerRotation.e();
                            }
                            else
                            {
                                if (E.transform.rotation.eulerAngles.y > 30)
                                {
                                    E.transform.rotation = Quaternion.Euler(0, 90, 0);
                                    layerRotation.eprime();
                                }
                                else
                                {
                                    E.transform.rotation = Quaternion.Euler(0, 0, 0);
                                }
                            }
                        }
                        R6.transform.parent = Cube2.transform;
                        R.transform.parent = Cube2.transform;
                        R4.transform.parent = Cube2.transform;
                        F.transform.parent = Cube2.transform;
                        F4.transform.parent = Cube2.transform;
                        L.transform.parent = Cube2.transform;
                        L4.transform.parent = Cube2.transform;
                        B.transform.parent = Cube2.transform;
                        E.transform.rotation = Quaternion.Euler(0, 0, 0);
                        rchild = R.transform.GetChild(0).gameObject;
                        rchild.transform.parent = null;
                        R.transform.rotation = Quaternion.Euler(0, 0, 0);
                        R.transform.position = new Vector3(2, 2, 0);
                        rchild.transform.parent = R.transform;
                        fchild = F.transform.GetChild(0).gameObject;
                        fchild.transform.parent = null;
                        F.transform.rotation = Quaternion.Euler(0, 0, 0);
                        F.transform.position = new Vector3(0, 2, -2);
                        fchild.transform.parent = F.transform;
                        lchild = L.transform.GetChild(0).gameObject;
                        lchild.transform.parent = null;
                        L.transform.rotation = Quaternion.Euler(0, 0, 0);
                        L.transform.position = new Vector3(-2, 2, 0);
                        lchild.transform.parent = L.transform;
                        bchild = B.transform.GetChild(0).gameObject;
                        bchild.transform.parent = null;
                        B.transform.rotation = Quaternion.Euler(0, 0, 0);
                        B.transform.position = new Vector3(0, 2, 2);
                        bchild.transform.parent = B.transform;

                    }
                    if (mousedir == 2)
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
                        // E
                        R6.transform.parent = E.transform;
                        R.transform.parent = E.transform;
                        R4.transform.parent = E.transform;
                        F.transform.parent = E.transform;
                        F4.transform.parent = E.transform;
                        L.transform.parent = E.transform;
                        L4.transform.parent = E.transform;
                        B.transform.parent = E.transform;
                        E.transform.Rotate(0, - speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (Mathf.Abs(deltapos.x) < Mathf.Abs(deltapos.y))
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
                        R.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                        mousedir = 2;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 275.5)
                    {
                        hasrotated = true;
                        E.transform.rotation = Quaternion.Euler(0, -90, 0);
                    }
                    if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 95.5)
                    {
                        hasrotated = true;
                        E.transform.rotation = Quaternion.Euler(0, 90, 0);
                    }
                    else
                    {
                        E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                    }
                }
                if (mousedir == 2)
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
                        R.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                    }
                }
            }
            if (Input.GetMouseButtonUp(0))
            {
                finalpos = Input.mousePosition;
                deltapos = finalpos - inicialpos;
                if (mousedir == 1)
                {
                    if (E.transform.rotation.eulerAngles.y > 330)
                    {
                        E.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (E.transform.rotation.eulerAngles.y > 265)
                        {
                            E.transform.rotation = Quaternion.Euler(0, -90, 0);
                            layerRotation.e();
                        }
                        else
                        {
                            if (E.transform.rotation.eulerAngles.y > 30)
                            {
                                E.transform.rotation = Quaternion.Euler(0, 90, 0);
                                layerRotation.eprime();
                            }
                            else
                            {
                                E.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    R6.transform.parent = Cube2.transform;
                    R.transform.parent = Cube2.transform;
                    R4.transform.parent = Cube2.transform;
                    F.transform.parent = Cube2.transform;
                    F4.transform.parent = Cube2.transform;
                    L.transform.parent = Cube2.transform;
                    L4.transform.parent = Cube2.transform;
                    B.transform.parent = Cube2.transform;
                    E.transform.rotation = Quaternion.Euler(0, 0, 0);
                    rchild = R.transform.GetChild(0).gameObject;
                    rchild.transform.parent = null;
                    R.transform.rotation = Quaternion.Euler(0, 0, 0);
                    R.transform.position = new Vector3(2, 2, 0);
                    rchild.transform.parent = R.transform;
                    fchild = F.transform.GetChild(0).gameObject;
                    fchild.transform.parent = null;
                    F.transform.rotation = Quaternion.Euler(0, 0, 0);
                    F.transform.position = new Vector3(0, 2, -2);
                    fchild.transform.parent = F.transform;
                    lchild = L.transform.GetChild(0).gameObject;
                    lchild.transform.parent = null;
                    L.transform.rotation = Quaternion.Euler(0, 0, 0);
                    L.transform.position = new Vector3(-2, 2, 0);
                    lchild.transform.parent = L.transform;
                    bchild = B.transform.GetChild(0).gameObject;
                    bchild.transform.parent = null;
                    B.transform.rotation = Quaternion.Euler(0, 0, 0);
                    B.transform.position = new Vector3(0, 2, 2);
                    bchild.transform.parent = B.transform;

                }
                if (mousedir == 2)
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
                hasrotated = false;
                mousedir = 0;
                pressed = false;
            }
        }       
    }
}
