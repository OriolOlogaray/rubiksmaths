using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fscript : MonoBehaviour
{
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject F;
    public GameObject U;
    public GameObject B;
    public GameObject D;
    public GameObject R;
    public GameObject L;
    public GameObject F2;
    public GameObject F8;
    public GameObject B2;
    public GameObject B8;
    public GameObject R4;
    public GameObject R6;
    public GameObject L4;
    public GameObject L6;
    public GameObject M;
    public GameObject E;
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
    GameObject uchild;
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
            if (F.transform.childCount > 0)
            {
                fchild = F.transform.GetChild(0).gameObject;
                Collider collf = fchild.GetComponentInChildren<Collider>();
                if (collf.Raycast(ray, out hit, 100.0f))
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
                    // E
                    R6.transform.parent = E.transform;
                    R.transform.parent = E.transform;
                    R4.transform.parent = E.transform;
                    F.transform.parent = E.transform;
                    L6.transform.parent = E.transform;
                    L.transform.parent = E.transform;
                    L4.transform.parent = E.transform;
                    B.transform.parent = E.transform;
                    E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                L6.transform.parent = Cube2.transform;
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
