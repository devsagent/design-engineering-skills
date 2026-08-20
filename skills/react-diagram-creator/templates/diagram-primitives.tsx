import { type ElementType, type ReactNode, useId } from "react";
import styles from "./diagram.module.css";

type HeadingLevel = 2 | 3 | 4 | 5 | 6;

type DiagramFrameProps = {
  anchorId?: string;
  headingLevel?: HeadingLevel;
  title: string;
  description: string;
  status: string;
  statusLive?: boolean;
  children: ReactNode;
  controls?: ReactNode;
  details?: ReactNode;
  detailsLabel?: string;
};

export function DiagramFrame({
  anchorId,
  headingLevel = 2,
  title,
  description,
  status,
  statusLive = false,
  children,
  controls,
  details,
  detailsLabel = "Diagram details",
}: DiagramFrameProps) {
  const instanceId = useId().replaceAll(":", "");
  const titleId = `diagram-title-${instanceId}`;
  const descriptionId = `diagram-description-${instanceId}`;
  const statusId = `diagram-status-${instanceId}`;
  const Heading = `h${headingLevel}` as ElementType;

  return (
    <section className={styles.section} aria-labelledby={titleId}>
      <header id={anchorId} className={styles.header}>
        <Heading id={titleId}>{title}</Heading>
        <p id={descriptionId}>{description}</p>
      </header>

      <figure
        className={styles.figure}
        aria-labelledby={titleId}
        aria-describedby={`${descriptionId} ${statusId}`}
      >
        <div className={styles.body}>
          <div className={styles.main}>{children}</div>
          {details ? (
            <div className={styles.details} role="group" aria-label={detailsLabel}>
              {details}
            </div>
          ) : null}
        </div>
        {controls ? <div className={styles.controls}>{controls}</div> : null}
        <figcaption
          id={statusId}
          className={styles.caption}
          aria-live={statusLive ? "polite" : undefined}
        >
          <span className={styles.statusDot} aria-hidden="true" />
          {status}
        </figcaption>
      </figure>
    </section>
  );
}

export function ControlGroup({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <div className={styles.controlGroup} role="group" aria-label={label}>
      <span className={styles.controlLabel}>{label}</span>
      <div className={styles.controlCluster}>{children}</div>
    </div>
  );
}

export function AccessibleSvg({
  title,
  description,
  viewBox,
  children,
  className,
}: {
  title: string;
  description: string;
  viewBox: string;
  children: ReactNode;
  className?: string;
}) {
  const titleId = useId();
  const descriptionId = useId();

  return (
    <svg
      className={[styles.diagramSvg, className].filter(Boolean).join(" ")}
      viewBox={viewBox}
      role="img"
      aria-labelledby={`${titleId} ${descriptionId}`}
    >
      <title id={titleId}>{title}</title>
      <desc id={descriptionId}>{description}</desc>
      {children}
    </svg>
  );
}

export function useSvgId(prefix: string) {
  const reactId = useId().replaceAll(":", "");
  return `${prefix}-${reactId}`;
}
