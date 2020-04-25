using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rscript : MonoBehaviour
{
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject F;
    public GameObject U;
    public GameObject B;
    public GameObject D;
    public GameObject R;
    public GameObject L;
    public GameObject R2;
    public GameObject R8;
    public GameObject L2;
    public GameObject L8;
    public GameObject R4;
    public GameObject R6;
    public GameObject L4;
    public GameObject L6;
    public GameObject S;
    public GameObject E;
    private int mousedir = 0;
    public int speed;
    public int correction = 50;
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
            if (R.transform.childCount > 0)
            {
                rchild = R.transform.GetChild(0).gameObject;
                Collider collr = rchild.GetComponentInChildren<Collider>();
                if (collr.Raycast(ray, out hit, 100.0f))
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
