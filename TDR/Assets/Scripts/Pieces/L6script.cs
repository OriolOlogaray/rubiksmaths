using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class L6script : MonoBehaviour
{
    public GameObject f4sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject F;
    public GameObject R4;
    public GameObject R;
    public GameObject R6;
    public GameObject B;
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
            if (L6.transform.childCount > 0)
            {
                Collider collf4 = f4sticker.GetComponentInChildren<Collider>();
                if (collf4.Raycast(ray, out hit, 100.0f))
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
                    // L
                    L1.transform.parent = L.transform;
                    L2.transform.parent = L.transform;
                    L3.transform.parent = L.transform;
                    L4.transform.parent = L.transform;
                    L6.transform.parent = L.transform;
                    L7.transform.parent = L.transform;
                    L8.transform.parent = L.transform;
                    L9.transform.parent = L.transform;
                    L.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
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
                if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 271.5)
                {
                    hasrotated = true;
                    L.transform.rotation = Quaternion.Euler(-90, 0, 0);
                }
                if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 91.5)
                {
                    hasrotated = true;
                    L.transform.rotation = Quaternion.Euler(90, 0, 0);
                }
                else
                {
                    L.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
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
                if (L.transform.rotation.eulerAngles.x > 330)
                {
                    L.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (L.transform.rotation.eulerAngles.x > 265)
                    {
                        L.transform.rotation = Quaternion.Euler(-90, 0, 0);
                        layerRotation.l();
                    }
                    else
                    {
                        if (L.transform.rotation.eulerAngles.x > 30)
                        {
                            L.transform.rotation = Quaternion.Euler(90, 0, 0);
                            layerRotation.lprime();
                        }
                        else
                        {
                            L.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                L1.transform.parent = Cube2.transform;
                L2.transform.parent = Cube2.transform;
                L3.transform.parent = Cube2.transform;
                L4.transform.parent = Cube2.transform;
                L6.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                L9.transform.parent = Cube2.transform;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
            }
            hasrotated = false;
            mousedir = 0;
            pressed = false;
        }
    }
}
