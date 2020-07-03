/* *************************************************************************************************************************************/
						/* *******requête d'extraction des informations sur les procédures et les dossiers **/
/* *************************************************************************************************************************************/

SELECT
    trunc(orchestra_dossier.date_creation) AS journee,
    COUNT(DISTINCT orchestra_dossier.id) AS nombre_de_dossier,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'SIGNATURE' THEN orchestra_dossier.id
        END
    ) ) AS nombre_de_signature,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN orchestra_dossier.id
        END
    ) ) AS nombre_de_ci,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN orchestra_dossier.id
        END
    ) ) AS nombre_de_rejection,
    COUNT(DISTINCT orchestra_dossier.id) - COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'SIGNATURE' THEN orchestra_dossier.id
        END
    ) ) - COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN orchestra_dossier.id
        END
    ) ) AS dossier_en_cours,
    orchestra_process.nom AS nom_procedure,
    orchestra_process.id AS id_procedure,
    webguce.core_good.good_hs_code,
    AVG(webguce.core_good.good_quantity) AS qte_moyenne,
    AVG(webguce.core_good.good_weight) AS poid_moyen,
    AVG(duration_) AS duree_moyenne
FROM
    ( ( ( ( ( orchestra.orchestra_dossier orchestra_dossier
    JOIN (
        SELECT
            id_,
            duration_
        FROM
            orchestra.jbpm4_hist_procinst
        WHERE
            duration_ IS NOT NULL
    ) jbpm4_hist_procinst ON orchestra_dossier.bpm_id = jbpm4_hist_procinst.id_ ) left
    JOIN orchestra.orchestra_message  orchestra_message ON orchestra_message.dossier_id = orchestra_dossier.id ) left
    JOIN orchestra.orchestra_message_type  orchestra_message_type ON orchestra_message.service_action = orchestra_message_type.message_type_id ) left
    JOIN orchestra.orchestra_process orchestra_process ON orchestra_dossier.process_id = orchestra_process.id ) left
    JOIN webguce.core_good ON orchestra_dossier.numero_dossier = webguce.core_good.record_id )
GROUP BY
    trunc(orchestra_dossier.date_creation),
    orchestra_process.nom,
    orchestra_process.id,
    webguce.core_good.good_hs_code;


/*ajouter :
nom du produit 
type
******fin
**/

/* *************************************************************************************************************************************/
/* *************************************requête d'extraction des  délais des procédures Ceci pour resoudre le problème sur 
**************************************************les calculs des quartiles et des moyennes   (quartiles ,avg)**************************************/
/* *************************************************************************************************************************************/
SELECT
    jbpm4_hist_procinst.start_,
    jbpm4_hist_procinst.duration_ / 3600 AS duration_,
    orchestra_charger.ch_name AS nom_chargeur,
    orchestra_charger.ch_niu AS niu_chargeur,
    jbpm4_id_user.id_ AS initialisateur_dossier,
    jbpm4_hist_procinst.quartile,
    orchestra_process.nom AS nom_procedure
FROM
    (
        SELECT
            id_,
            duration_,
            jbpm4_hist_procinst.start_,
            NTILE(4) OVER(
                ORDER BY
                    jbpm4_hist_procinst.duration_ DESC
            ) AS quartile
        FROM
            orchestra.jbpm4_hist_procinst
        WHERE
            duration_ IS NOT NULL
    ) jbpm4_hist_procinst
    JOIN orchestra.orchestra_dossier orchestra_dossier ON orchestra_dossier.bpm_id = jbpm4_hist_procinst.id_
    JOIN orchestra.jbpm4_id_user jbpm4_id_user ON jbpm4_id_user.dbid_ = orchestra_dossier.initializer
    LEFT JOIN orchestra.orchestra_charger orchestra_charger ON orchestra_charger.ch_code = orchestra_dossier.charger
    LEFT JOIN orchestra.orchestra_process orchestra_process ON orchestra_dossier.process_id = orchestra_process.id;
     

	 

	 
	 
	 
	 
	 
/* *************************************************************************************************************************************/
/* *************************************Indicateur Doing Business
**************************************************import et export**************************************/
/* *************************************************************************************************************************************/
 
	 
	 
	 
	 
	 
SELECT
    jbpm4_hist_procinst.start_,
    jbpm4_hist_procinst.duration_ / 3600000 AS duration_,
    orchestra_charger.ch_name AS nom_chargeur,
    orchestra_charger.ch_niu AS niu_chargeur,
    jbpm4_id_user.id_ AS initialisateur_dossier,
    jbpm4_hist_procinst.quartile,
    orchestra_process.nom AS nom_procedure,
    NUMERO_DOSSIER,
    webguce.core_good.GOOD_HS_CODE,
    WEBGUCE.PRED_REGISTRATION.FOB_AMOUNT_CFA,
    sp.position as sh_position,
    sc.TITRE as chapter_title ,
    ss.TITRE as section_title,
    orchestra.orchestra_process.id as  process_id,


FROM
    (
        SELECT
            id_,
            duration_,
            jbpm4_hist_procinst.start_,
            NTILE(4) OVER(
                ORDER BY
                    jbpm4_hist_procinst.duration_ DESC
            ) AS quartile
        FROM
            orchestra.jbpm4_hist_procinst
        WHERE
            duration_ IS NOT NULL
    ) jbpm4_hist_procinst
    JOIN orchestra.orchestra_dossier orchestra_dossier ON orchestra_dossier.bpm_id = jbpm4_hist_procinst.id_
    JOIN orchestra.jbpm4_id_user jbpm4_id_user ON jbpm4_id_user.dbid_ = orchestra_dossier.initializer
    LEFT JOIN orchestra.orchestra_charger orchestra_charger ON orchestra_charger.ch_code = orchestra_dossier.charger
    LEFT JOIN orchestra.orchestra_process orchestra_process ON orchestra_dossier.process_id = orchestra_process.id
    left JOIN webguce.core_good ON orchestra_dossier.numero_dossier = webguce.core_good.record_id
    left JOIN WEBGUCE.PRED_REGISTRATION ON orchestra_dossier.numero_dossier = WEBGUCE.PRED_REGISTRATION.record_id
    left join webguce.sh_position sp on core_good.good_hs_code||0= sp.CODE_DE_SH
    left join webguce.sh_chapter sc on sp.chapitre= sc.NUMERO
    left join webguce.SH_SECTION_ ss on ss.NUMERO=sp.SECTION 
    where  sp.position=8708
    ;

	 
	 
	 
	 
	 
	 
	 
	 
	 
SELECT
    jbpm4_hist_procinst.start_,
    jbpm4_hist_procinst.duration_ / 3600000 AS duration_,
    orchestra_charger.ch_name AS nom_chargeur,
    orchestra_charger.ch_niu AS niu_chargeur,
    jbpm4_id_user.id_ AS initialisateur_dossier,
    jbpm4_hist_procinst.quartile,
    orchestra_process.nom AS nom_procedure,
    NUMERO_DOSSIER,
    webguce.core_good.GOOD_HS_CODE,
    WEBGUCE.EXPRED_CARG_REGISTRATION.ECG_FOB_AMOUNT_CFA,
    sp.position as sh_position,
    sc.TITRE as chapter_title ,
    ss.TITRE as section_title,
	orchestra.orchestra_process.id as  process_id,


FROM
    (
        SELECT
            id_,
            duration_,
            jbpm4_hist_procinst.start_,
            NTILE(4) OVER(
                ORDER BY
                    jbpm4_hist_procinst.duration_ DESC
            ) AS quartile
        FROM
            orchestra.jbpm4_hist_procinst
        WHERE
            duration_ IS NOT NULL
    ) jbpm4_hist_procinst
    JOIN orchestra.orchestra_dossier orchestra_dossier ON orchestra_dossier.bpm_id = jbpm4_hist_procinst.id_
    JOIN orchestra.jbpm4_id_user jbpm4_id_user ON jbpm4_id_user.dbid_ = orchestra_dossier.initializer
    LEFT JOIN orchestra.orchestra_charger orchestra_charger ON orchestra_charger.ch_code = orchestra_dossier.charger
    LEFT JOIN orchestra.orchestra_process orchestra_process ON orchestra_dossier.process_id = orchestra_process.id
    left JOIN webguce.core_good ON orchestra_dossier.numero_dossier = webguce.core_good.record_id
    left JOIN WEBGUCE.EXPRED_CARG_REGISTRATION ON orchestra_dossier.numero_dossier = WEBGUCE.EXPRED_CARG_REGISTRATION.record_id
    left join webguce.sh_position sp on core_good.good_hs_code||0= sp.CODE_DE_SH
    left join webguce.sh_chapter sc on sp.chapitre= sc.NUMERO
    left join webguce.SH_SECTION_ ss on ss.NUMERO=sp.SECTION 
    where  sp.position=1801
    ;

	
	
	
	
	
/* *************************************************************************************************************************************/
        /*  *******************************requête d'extraction des informations sur les partenaires **/
/* *************************************************************************************************************************************/




SELECT
    trunc(jbpm4_hist_task.create_),
    COUNT(DISTINCT jbpm4_hist_task.dbid_) AS nombre_de_taches,
    AVG(jbpm4_hist_task.duration_ / 3600) AS duration_traitement,
    jbpm4_hist_task.assignee_,
    COUNT(DISTINCT orchestra_dossier.id) AS nombre_de_dossiers,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'SIGNATURE' THEN jbpm4_hist_task.dbid_
        END
    ) ) AS nombre_de_signature,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN jbpm4_hist_task.dbid_
        END
    ) ) AS nombre_de_ci,
    COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN jbpm4_hist_task.dbid_
        END
    ) ) AS nombre_de_rejection,
    COUNT(DISTINCT orchestra_dossier.id) - COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'SIGNATURE' THEN orchestra_dossier.date_creation
        END
    ) ) - COUNT(DISTINCT(
        CASE
            WHEN orchestra_message_type.message_type_category = 'CI_REQUEST' THEN orchestra_dossier.date_creation
        END
    ) ) AS dossier_en_cours,
    orchestra_message_type.message_type_category AS etat_des_dossiers,
    orchestra_process.nom AS procedure,
    orchestra_process.id,
    orchestra_charger.ch_name AS nom_chargeur,
    orchestra_charger.ch_niu AS niu_chargeur,
    jbpm4_id_user.id_ AS initialisateur_dossier,
    webguce.core_good.good_hs_code,
    webguce.core_good.good_quantity,
    webguce.core_good.good_weight,
    jbpm4_hist_actinst.activity_name_
FROM
    ( ( ( ( ( ( ( ( orchestra.jbpm4_hist_task jbpm4_hist_task
    JOIN orchestra.jbpm4_hist_actinst jbpm4_hist_actinst ON jbpm4_hist_task.dbid_ = jbpm4_hist_actinst.htask_ )
    JOIN orchestra.jbpm4_hist_procinst jbpm4_hist_procinst ON jbpm4_hist_actinst.hproci_ = jbpm4_hist_procinst.dbid_ )
    JOIN orchestra.orchestra_dossier orchestra_dossier ON orchestra_dossier.bpm_id = jbpm4_hist_procinst.id_ )
    JOIN orchestra.orchestra_process orchestra_process ON orchestra_dossier.process_id = orchestra_process.id )
    JOIN orchestra.jbpm4_id_user jbpm4_id_user ON jbpm4_id_user.dbid_ = orchestra_dossier.initializer ) left
    JOIN orchestra.orchestra_charger orchestra_charger ON orchestra_charger.ch_code = orchestra_dossier.charger ) left
    JOIN orchestra.orchestra_message orchestra_message ON orchestra_message.dossier_id = orchestra_dossier.id ) left
    JOIN orchestra.orchestra_message_type orchestra_message_type ON orchestra_message.service_action = orchestra_message_type.message_type_id
) left
    JOIN webguce.core_good ON orchestra_dossier.numero_dossier = webguce.core_good.record_id
GROUP BY
    trunc(jbpm4_hist_task.create_),
    jbpm4_hist_task.assignee_,
    orchestra_message_type.message_type_category,
    orchestra_process.nom,
    orchestra_process.id,
    orchestra_charger.ch_name,
    jbpm4_id_user.id_,
    orchestra_charger.ch_niu,
    webguce.core_good.good_hs_code,
    webguce.core_good.good_quantity,
    webguce.core_good.good_weight,
    jbpm4_hist_actinst.activity_name_