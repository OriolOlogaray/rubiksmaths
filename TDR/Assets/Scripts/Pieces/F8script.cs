using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class F8script : MonoBehaviour
{
    public GameObject f8sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject L9;
    public GameObject F8;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject B8;
    public GameObject L7;
    public GameObject L8;
    public GameObject F;
    public GameObject F2;
    public GameObject U;
    public GameObject B2;
    public GameObject B;
    public GameObject D;
    public GameObject M;
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
            if (F8.transform.childCount > 0)
            {
                Collider collf8 = f8sticker.GetComponentInChildren<Collider>();
                if (collf8.Raycast(ray, out hit, 100.0f))
                {
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
            }
        }
        if (pressed == true && !hasrotated)
        {
            if (mousedir == 0)
            {
                deltapos = Input.mousePosition - inicialpos;
                if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                {
                    // D
                    L9.transform.parent = D.transform;
                    F8.transform.parent = D.transform;
                    R7.transform.parent = D.transform;
                    R8.transform.parent = D.transform;
                    R9.transform.parent = D.transform;
                    B8.transform.parent = D.transform;
                    L7.transform.parent = D.transform;
                    L8.transform.parent = D.transform;
                    D.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 275.5)
                {
                    hasrotated = true;
                    D.transform.rotation = Quaternion.Euler(0, -90, 0);
                }
                if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 95.5)
                {
                    hasrotated = true;
                    D.transform.rotation = Quaternion.Euler(0, 90, 0);
                }
                else
                {
                    D.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                if (D.transform.rotation.eulerAngles.y > 330)
                {
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (D.transform.rotation.eulerAngles.y > 265)
                    {
                        D.transform.rotation = Quaternion.Euler(0, -90, 0);
                        layerRotation.d();
                    }
                    else
                    {
                        if (D.transform.rotation.eulerAngles.y > 30)
                        {
                            D.transform.rotation = Quaternion.Euler(0, 90, 0);
                            layerRotation.dprime();
                        }
                        else
                        {
                            D.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                L9.transform.parent = Cube2.transform;
                F8.transform.parent = Cube2.transform;
                R7.transform.parent = Cube2.transform;
                R8.transform.parent = Cube2.transform;
                R9.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
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
